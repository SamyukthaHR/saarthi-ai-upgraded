
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_gemma(prompt: str):
    payload = {
        "model": "gemma:2b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()["response"]
