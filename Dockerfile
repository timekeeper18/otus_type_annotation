FROM python:3.12-slim

# Временнуя зона
ENV TZ=UTC \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Системные зависимости и timezone
RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

WORKDIR /otus_type_annotation

COPY poetry.lock poetry.toml pyproject.toml ./

# Зависимости проекта
RUN poetry install --no-root

# Исходный код
COPY ./basic ./basic
COPY ./intermediate ./intermediate

# Команда для запуска
CMD ["poetry", "run", "mypy", "."]