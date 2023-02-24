# Install system dependencies
FROM python:3.10-buster
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

# Copy across codebase
COPY todo_app /todo-app/todo_app
COPY tests /todo-app/tests
COPY .env.test /todo-app
COPY poetry.lock /todo-app
COPY poetry.toml /todo-app
COPY pyproject.toml /todo-app

# Install package dependencies
    # TODO exercise-5: Figure out how to add poetry to your path from the command line -> ~/.local/share/pypoetry/venv/bin/poetry
WORKDIR /todo-app
RUN ~/.local/share/pypoetry/venv/bin/poetry install

# Run app
EXPOSE 8088
ENTRYPOINT ~/.local/share/pypoetry/venv/bin/poetry run gunicorn --bind 0.0.0.0:8088 "todo_app.app:create_app()"







## DELETE THIS AFTER DEV COMPLETE / add it to the readme
# docker build --tag todo-app .
# docker run -d --env-file .env --publish 8081:8088 todo-app