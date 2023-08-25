import logging

from todo_app.config.flask_config import FlaskConfig
from loggly.handlers import HTTPSHandler
from logging import Formatter


def configure_logs(config: FlaskConfig):
    # Apply global logging configuration.
    logger = logging.getLogger("azure_todo_app")
    logger.setLevel(config.DEFAULT_LOG_LEVEL)
    
    handler = HTTPSHandler(f'https://logs-01.loggly.com/inputs/{config.LOGGLY_TOKEN}/tag/todo-app')
    handler.setFormatter(
        Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
    )
    logger.addHandler(handler)
