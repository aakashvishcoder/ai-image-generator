from fastapi import APIRouter
from pydantic import BaseModel
import asyncio
from concurrent.futures import ThreadPoolExecutor
from .replicate_client import generate_image_url_blocking

router = APIRouter()
executor = ThreadPoolExecutor(max_workers=3)

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
async def generate(prompt_request: PromptRequest):
    result = await asyncio.get_running_loop().run_in_executor(
        executor,
        generate_image_url_blocking,
        prompt_request.prompt,
    )
    return result
