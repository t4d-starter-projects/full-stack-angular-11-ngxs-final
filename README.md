# Mastering Full-Stack Development with Angular 11 Series on WintellectNOW

This is the final version of the ngxs project.

## Prerequisites

Install Docker for Windows or Docker for Mac - https://www.docker.com/products/docker-desktop

## Run Backend Services for Front-End Development

To run the backend services, run the following command from a terminal window. The command must be executed from the same folder as the `docker-compose.yml` file.

```bash
docker-compose up -d
```

## Run Database and Web Server only for Backend and Front-End Development

You will need to have Python 3 and Pipenv installed.

Download and Install Python 3: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Download and Install Pipenv: [https://pipenv.pypa.io/en/latest/install/#installing-pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)

After Python 3 and Pipenv are installed, to do development on both the backend REST API and the front-end UI application, the Docker Compose configuration file named `docker-compose-dev.yml` should be used instead of the default `docker-compose.yml` file. The `docker-compose-dev.yml` file only starts the web server and the database server. The backend application (coded in Python using Flask) can then be edited and executed from an IDE such as [PyCharm](https://www.jetbrains.com/pycharm/). To run Docker Compose with the alternate configuration file, open a terminal window, change to the folder where you cloned this repository, and run the following command.

```bash
docker-compose -f ./docker-compose-dev.yml up -d
```

To run the backend, `backend/config.ini` configuration file will need to be modified.

Modify the following entry:

```
[database]
url=host.docker.internal:5432
```

To be this:

```
[database]
url=localhost:5432
```

Now run the backend, and you will have a full development environment. If you are unsure how to run the backend, watch the following [video](https://vimeo.com/482656478/6840d08c14) which explains how to run the backend with PyCharm.



## What about the Front-End?

The Front-End UI application will be created in the course you are taking. The purpose of the backend is to provide a REST API and user authentication/authorization mechanism for the Front-End UI application.

