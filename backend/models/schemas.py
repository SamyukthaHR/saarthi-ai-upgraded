
from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: str
    question: str
    level: str = "beginner"
    language: str = "english"
