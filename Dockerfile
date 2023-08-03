FROM python:3.11.4-alpine3.18

WORKDIR /app

RUN python3 -m venv /opt/venv

COPY . /app
COPY . /config

RUN apk update
RUN apk add --virtual build-deps 
RUN apk add gcc 
RUN apk add musl-dev
RUN apk add --no-cache mariadb-dev
RUN apk add libffi-dev

RUN pip3 install --upgrade pip
RUN . /opt/venv/bin/activate && pip3 install -r requirements.txt

EXPOSE 9090

CMD . /opt/venv/bin/activate && exec flask run -h 0.0.0.0 -p 9090