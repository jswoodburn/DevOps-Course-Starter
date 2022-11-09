# Install dependencies
FROM python:3.10-buster
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
RUN poetry install

# Copy across codebase
    # TODO exercise-5: don't copy files you don't need
COPY . /todo-app

EXPOSE 8088

# Run app
    # TODO exercise-5: This means adding gunicorn to your list of dependencies, and setting an entrypoint like the following
RUN poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

ENTRYPOINT ["java", "-javaagent:/opt/newrelic/newrelic.jar", "-jar", "membership-signup-service.jar"]
