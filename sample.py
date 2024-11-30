import os
import requests

url = "http://localhost:8000"  
hf_token = os.getenv("HF_TOKEN").strip()
query_payload = {
    "hf_token": hf_token,
    "query": {
        "messages": [
            {"role": "user", "content": "What is Qwen?"},
        ],
        "temperature": 0.7,
        "max_tokens": 10000,
        "top_p": 0.7,
        "stream": True,
    },
}

response = requests.post(url, json=query_payload, stream=True, headers={
    "Content-Type": "application/json"
})

if response.status_code == 200:
    print("Streaming response:")
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            print(chunk.decode("utf-8"), end="", flush=True)
else:
    print(f"Error: {response.status_code} - {response.text}")
