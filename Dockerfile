FROM python:3.7.0

# Copy requirements file in separately to rest of project.
# This allows docker to cache requirements, and so only changes to
# requirements.txt will trigger a new pip install
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD . /jawbbone-health-example
WORKDIR /jawbbone-health-example

ENV PYTHONPATH=/jawbbone-health-example:$PYTHONPATH