from fastapi import APIRouter
from .schemas import PromptRequest
from .openaiclient import generate_image

router = APIRouter()

@router.post("/generate")
async def generate(prompt: PromptRequest):
    return await generate_image(prompt.prompt)