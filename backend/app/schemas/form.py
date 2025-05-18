from pydantic import BaseModel
from typing import List, Optional

class Question(BaseModel):
    text: str
    type: str  # e.g., text, select, rating, boolean
    options: Optional[List[str]] = None

class Form(BaseModel):
    id: Optional[str]
    name: str
    version: int
    questions: List[Question]

