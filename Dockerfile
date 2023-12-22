# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip3 install --upgrade pip

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install the requirements
COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . .

# initialize the database (create DB, tables, populate)
RUN python init_db.py

EXPOSE 8080/tcp

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "app:app"]
