import logging

def configure_logs():
    # Apply global logging configuration.
    # Run this at the root of every function.

    logging.getLogger("azure_todo_app").setLevel(logging.WARNING)
