.PHONY: help
help:
	@echo "Available commands:"
	@echo "\tclean - stop the running containers and remove pycache folders"
	@echo "\tcreate-env-files - Create local env files"
	@echo "\tbuild - build application"
	@echo "\tstart - run program"
	@echo "\tstart - stop program"
	@echo "\ttests - run tests"
	@echo "\tlint - run lint"
	@echo "\texternal_lint - run the jawbone linter"
	@echo "\tget_latest_rates - Get a print out of the latest exchange rates"

.PHONY: clean
clean:
	-find . -type d -name '__pycache__' -exec rm -rf {} ';'
	docker-compose down

.PHONY: create-env-file
create-env-files:
ifeq ("$(wildcard .env)","")
	@echo "POSTGRES_USER=jawbone" > .env
	@echo "POSTGRES_PASSWORD=CHANGEME" >> .env
	@echo "FIXERIO_API_KEY=CHANGEME" >> .env
endif

.PHONY: build
build: clean create-env-files
	docker-compose build

.PHONY: start
start: build
	docker-compose up

.PHONY: stop
stop:
	docker-compose down

.PHONY: tests
tests: build
	docker-compose run web bash -c "py.test -s --disable-warnings ."

.PHONY: lint
lint: build
	docker-compose run web bash -c "flake8 ."

.PHONY: external_lint
external_lint: build
	docker-compose run web bash -c "curl https://gist.githubusercontent.com/richardARPANET/79434d9995585f639344e17c35476728/raw/36e9ca68088ee7832220a20c31997a25a0bbd271/lint.sh | sh"

.PHONY: get_latest_rates
get_latest_rates: build
	docker-compose run web bash -c "flask get_latest_rate"
