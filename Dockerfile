FROM python:3.8

RUN apt-get update && \
    apt-get install -y git

ADD requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && \
    rm -f requirements.txt

WORKDIR "/opt/working"
