from sqlalchemy.orm import sessionmaker
from db.DBEngine import DBEngine

# Create the database engine (singleton)
engine = DBEngine("sqlite+pysqlite:///./database.db").get_engine()
    
# Set up the session factory
SessionLocal = sessionmaker(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
