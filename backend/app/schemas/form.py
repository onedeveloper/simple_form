from pydantic import BaseModel
from typing import List, Optional

class QuestionSchema(BaseModel):
    label: str
    type: str  # e.g., text, select, rating, boolean
    options: Optional[List[str]] = None

class FormSchema(BaseModel):
    id: Optional[str] = None
    name: str
    questions: List[QuestionSchema]

