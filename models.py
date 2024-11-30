from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str

class Query(BaseModel):
    messages: list[Message]
    temperature: float = 0.5
    max_tokens: int = 10200
    top_p: float = 0.7
    stream: bool = False