from typing import List
from pydantic import BaseModel, ConfigDict

class ORMModel(BaseModel):
    # Useful config for automatically converting from SQLAlchemy models into Pydantic
    model_config = ConfigDict(from_attributes=True)

class WineModel(ORMModel):
    id: int
    name: str

class WineResponseModel(ORMModel):
    wines: List[WineModel]

class WineRequestModel(BaseModel):
    name: str