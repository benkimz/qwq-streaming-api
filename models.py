from typing import List, Optional
from pydantic import BaseModel

from pydantic import BaseModel

class Message(BaseModel):
    role: Optional[str] = None
    content: Optional[str] = None

class Query(BaseModel):
    messages: List[Message] = []
    temperature: float = 0.5
    max_tokens: int = 10200
    top_p: float = 0.7
    stream: bool = False

class QueryRequest(BaseModel):
    query: Query
    hf_token: str
