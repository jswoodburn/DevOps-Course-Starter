# Install system dependencies
FROM python:3.10-buster AS base
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

FROM base AS production

# Run app
EXPOSE 8088
ENTRYPOINT ~/.local/share/pypoetry/venv/bin/poetry run gunicorn --bind 0.0.0.0:8088 "todo_app.app:create_app()"

FROM base AS development

ENTRYPOINT ~/.local/share/pypoetry/venv/bin/poetry run flask run --host 0.0.0.0





## DELETE THIS AFTER DEV COMPLETE / add it to the readme
# docker build --tag todo-app .
# docker run -d --env-file .env --publish 8081:8088 todo-app // detached
# docker run -it --env-file .env --publish 8081:8088 todo-app // with logs

# docker build --target development --tag todo-app:dev .
# this is 5000 not 8088 because flask runs on 5000 by default so is on 5000 of the container's "localhost"
# docker run -it --env-file .env --publish 8081:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/todo-app/todo_app todo-app:dev

# docker build --target production --tag todo-app:prod .
# docker run -it --env-file .env --publish 8081:8088 todo-app:prod




