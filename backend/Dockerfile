FROM python:3.9

ENV FLASK_APP=./src/main.py

RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pipenv install --deploy --ignore-pipfile

COPY src ./src
COPY config.ini ./

CMD [ "pipenv", "run", "flask", "run", "--host=0.0.0.0" ]
