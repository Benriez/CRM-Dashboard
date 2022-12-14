FROM python:3.11-rc-alpine
RUN apk update && apk upgrade && apk add --no-cache make g++ bash git openssh postgresql-dev curl
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./django_project/ /usr/src/app
RUN pip install -r requirements.txt
COPY ./utils/ /usr/src/utils
EXPOSE 80
CMD sh /usr/src/utils/run.sh