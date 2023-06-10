FROM python:3.10-slim

WORKDIR /code

RUN apt-get update -qq  \
    && apt-get -y install ffmpeg

RUN pip3 install poetry
ENV POETRY_NO_INTERACTION=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false

RUN poetry install -n --no-ansi

COPY . .

CMD poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000
