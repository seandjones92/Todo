FROM python:3.7.2-alpine

LABEL Name=todo Version=0.0.1
EXPOSE 3000

WORKDIR /app
ADD . /app

RUN apk add gcc musl-dev
RUN python3 -m pip install pipenv
RUN pipenv install --ignore-pipfile

# For 'production' you should use a WSGI server instead
CMD [ "pipenv", "run", "python", "todo" ]
