
from fastapi import FastAPI
from backend.routes.chat import router as chat_router
from backend.routes.pdf import router as pdf_router

app = FastAPI(title="Offline AI Tutor - Saarthi AI")

app.include_router(chat_router)
app.include_router(pdf_router)

@app.get("/")
def health():
    return {"status": "running"}
