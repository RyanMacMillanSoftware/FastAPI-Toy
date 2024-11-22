from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

class DBEngine:
    _instance = None

    def __init__(self, connection_string: str):
        if DBEngine._instance is not None:
            raise Exception("This class is a singleton!")
        self._engine = create_engine(connection_string)
        DBEngine._instance = self

    @classmethod
    def get_engine(cls, connection_string: str = None) -> Engine:
        """Get the singleton database engine instance."""
        if cls._instance is None:
            if not connection_string:
                raise ValueError("A connection string must be provided for the first initialization.")
            cls(connection_string)  # Initialize the singleton
        return cls._instance._engine
