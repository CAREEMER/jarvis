FROM python:3.9.6-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update \
  && pip install --upgrade pip \
  && pip install poetry==1.1.6 \
  && apt install ffmpeg flac -y

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

ARG BOT_TOKEN

ENV BOT_TOKEN="${BOT_TOKEN}"

COPY . .

ENTRYPOINT ["python", "main.py"]
