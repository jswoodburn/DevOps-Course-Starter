import logging

from todo_app.config.flask_config import FlaskConfig


def configure_logs(config: FlaskConfig):
    # Apply global logging configuration.
    logging.getLogger("azure_todo_app").setLevel(config.DEFAULT_LOG_LEVEL)
