from fastapi import FastAPI

from fastapi.responses import StreamingResponse
from huggingface_hub import InferenceClient

from models import QueryRequest

app = FastAPI()


@app.post("/")
async def query_model(qreq: QueryRequest):

    client = InferenceClient(api_key=qreq.hf_token)

    messages = [message.model_dump() for message in qreq.query.messages]
    
    async def chat_stream():
        stream = client.chat.completions.create(
            model="Qwen/QwQ-32B-Preview",
            messages=messages,
            temperature=qreq.query.temperature,
            max_tokens=qreq.query.max_tokens,
            top_p=qreq.query.top_p,
            stream=qreq.query.stream
        )    
        for chunk in stream:
            yield chunk.choices[0].delta.content

    return StreamingResponse(chat_stream(), media_type="text/plain")    