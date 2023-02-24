# Install system dependencies
FROM python:3.10-buster AS base
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

# Copy across dependecy management files
WORKDIR /todo-app
COPY poetry.lock /todo-app
COPY pyproject.toml /todo-app

# Install package dependencies
RUN ~/.local/share/pypoetry/venv/bin/poetry install

# Copy across code
COPY poetry.toml /todo-app
COPY todo_app /todo-app/todo_app
COPY tests /todo-app/tests
COPY .env.test /todo-app

FROM base AS production

# Run app
EXPOSE 8088
ENTRYPOINT ~/.local/share/pypoetry/venv/bin/poetry run gunicorn --bind 0.0.0.0:8088 "todo_app.app:create_app()"

FROM base AS development

ENTRYPOINT ~/.local/share/pypoetry/venv/bin/poetry run flask run --host 0.0.0.0

FROM base as tests

ENTRYPOINT ~/.local/share/pypoetry/venv/bin/poetry run pytest tests
