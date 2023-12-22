# syntax=docker/dockerfile:1.4
FROM python:3.9-slim

# Atualiza a lista de pacotes
RUN apt-get update && apt-get install -y \
    # Pacotes adicionais, se necessário
    && rm -rf /var/lib/apt/lists/*

ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install the requirements
COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Copia apenas os arquivos necessários
COPY . .

EXPOSE 80/tcp

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:80", "app:app"]
