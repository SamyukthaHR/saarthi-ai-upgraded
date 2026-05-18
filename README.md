
# Saarthi AI - Offline Tutor

## Features
- Offline LLM (Gemma via Ollama)
- RAG (uses study material)
- Multilingual (English, Hindi, Kannada)
- Student memory

## Setup

1. Install Ollama and run:
   ollama run gemma

2. Install dependencies:
   pip install -r requirements.txt

3. Run backend:
   uvicorn backend.app:app --reload

4. Run frontend:
   streamlit run frontend/app.py
