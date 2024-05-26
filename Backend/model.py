from typing import List
from pydantic import BaseModel
# Define your data models
class Document(BaseModel):
    name: str
    text: str
    embedding: List[float]