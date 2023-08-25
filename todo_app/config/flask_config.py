import os


class FlaskConfig:
    def __init__(self):
        """Base configuration variables."""
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        if not self.SECRET_KEY:
            raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
        
        self.DEFAULT_LOG_LEVEL = os.environ.get('DEFAULT_LOG_LEVEL')
        if not self.DEFAULT_LOG_LEVEL:
            raise ValueError("No DEFAULT_LOG_LEVEL set for Flask logging.")
