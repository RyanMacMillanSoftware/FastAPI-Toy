from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from db.models import Wine
from wine_models import WineResponse
from db.session import get_db 
from db.models import create_db_tables
from db.DBEngine import DBEngine

# Instantiate API
app = FastAPI()

# Create DB tables from ORM schema
create_db_tables(DBEngine.get_engine())

# Define the GET /wines endpoint
@app.get("/wines", response_model=WineResponse)
def get_all_wines(db: Session = Depends(get_db)):
    wines = db.query(Wine).all()
    return WineResponse(wines=wines)
