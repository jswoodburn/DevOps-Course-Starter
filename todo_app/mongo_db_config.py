import os


class MongoDbConfig:
    def __init__(self):
        """MongoDB configuration variables."""
        self.COSMOS_CONNECTION_STRING = os.environ.get(
            'COSMOS_CONNECTION_STRING'
        )
        if not self.COSMOS_CONNECTION_STRING:
            raise ValueError(
                "No COSMOS_CONNECTION_STRING set for MongoDB configuration."
            )

        self.COSMOS_DB_NAME = os.environ.get('COSMOS_DB_NAME')
        if not self.COSMOS_DB_NAME:
            raise ValueError("No COSMOS_DB_NAME set for MongoDB configuration.")