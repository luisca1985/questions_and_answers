ARG PYTHON_VERSION=3.9-slim-bullseye

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

ARG APP_HOME=/app

WORKDIR ${APP_HOME}


# Requirements are installed here to ensure they will be cached.
COPY requirements.txt ${APP_HOME}/requirements.txt

# Dependencies
RUN pip3 install -r requirements.txt

# copy application code to WORKDIR
COPY . ${APP_HOME}

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]

