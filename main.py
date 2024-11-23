from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

from db.models import Wine
from wine_models import WineModel, WineRequestModel, WineResponseModel
from db.session import get_db 
from db.models import create_db_tables
from db.DBEngine import DBEngine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create DB tables from ORM schema
    create_db_tables(DBEngine.get_engine())
    yield

app = FastAPI(lifespan=lifespan)

# Define the GET /wines endpoint
@app.get("/wines/", response_model=WineResponseModel)
def get_all_wines(db: Session = Depends(get_db)):
    results = db.query(Wine).all()
    return WineResponseModel(wines=results)

# Define the POST /wines endpoint
@app.post("/wines/", response_model = WineModel, status_code=status.HTTP_201_CREATED)
def add_wine(wine: WineRequestModel, db: Session = Depends(get_db)):
    new_wine = Wine(name = wine.name)
    db.add(new_wine)
    db.commit()
    db.refresh(new_wine)
    return new_wine
