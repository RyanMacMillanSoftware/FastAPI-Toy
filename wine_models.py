from typing import List
from pydantic import BaseModel

class Wine(BaseModel):
    id: int
    name: str

class WineResponse(BaseModel):
    wines: List[Wine]
