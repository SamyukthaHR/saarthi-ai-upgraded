
from fastapi import APIRouter
from backend.models.schemas import ChatRequest
from backend.services.llm_service import query_gemma
from backend.services.prompt_engine import build_prompt
from backend.services.rag_service import retrieve_context
from backend.services.memory_service import get_history, store_interaction

router = APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):
    language_prompts = {
    "English": "Answer in English",
    "Hindi": "Answer in Hindi",
    "Kannada": "Answer in Kannada"
    }

    instruction = language_prompts.get(req.language, "")

    final_prompt = f"""
    {instruction}

    Question:
    {req.question}
    """
    history = get_history(req.user_id)
    context = retrieve_context(req.question)
    print(req.question, req.level, req.language)

    prompt = build_prompt(
        question=req.question,
        level=req.level,
        language=req.language,
        # context=context,
        history=history
    )
    print(prompt)

    response = query_gemma(prompt)
    store_interaction(req.user_id, req.question)

    return {"answer": response}
