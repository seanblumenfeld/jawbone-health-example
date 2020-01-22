.PHONY: help
help:
	@echo "Available commands:"
	@echo "\tclean - stop the running containers and remove pycache folders"
	@echo "\tbuild - build application"
	@echo "\tstart - run program"
	@echo "\ttests - run tests"
	@echo "\tlint - run flake8"

.PHONY: clean
clean:
	find . -type d -name '__pycache__' -exec rm -f {} ';'
	docker-compose down

.PHONY: create-env-files
create-env-files:
ifeq ("$(wildcard db.env)","")
	@echo "POSTGRES_USER=jawbone" > db.env
	@echo "POSTGRES_PASSWORD=CHANGEME" >> db.env
endif

.PHONY: build
build: clean
	docker-compose build

.PHONY: start
start: build
	docker-compose up

.PHONY: stop
stop:
	docker-compose down

.PHONY: tests
tests: build
	docker-compose run jawbone_health_example bash -c "py.test ."

.PHONY: lint
lint:
	docker-compose run jawbone_health_example bash -c "flake8 ."
