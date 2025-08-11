from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from concurrent.futures import ThreadPoolExecutor
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import io
import requests

# Load environment variables
load_dotenv()

app = FastAPI()

executor = ThreadPoolExecutor()

HF_API_KEY = os.getenv("HF_API_KEY")
CLOUDINARY_UPLOAD_URL = os.getenv("CLOUDINARY_UPLOAD_URL")  # Your full Cloudinary upload URL

hf_client = InferenceClient(provider="fal-ai", api_key=HF_API_KEY)

class Prompt(BaseModel):
    prompt: str

CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_UPLOAD_PRESET = os.getenv("CLOUDINARY_UPLOAD_PRESET")
CLOUDINARY_UPLOAD_URL = f"https://api.cloudinary.com/v1_1/{CLOUDINARY_CLOUD_NAME}/image/upload"

def generate_image_url_blocking(prompt: str):
    image = hf_client.text_to_image(prompt, model="Qwen/Qwen-Image")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    files = {"file": ("image.png", buffer, "image/png")}
    data = {"upload_preset": CLOUDINARY_UPLOAD_PRESET}

    response = requests.post(CLOUDINARY_UPLOAD_URL, files=files, data=data)
    if response.status_code == 200:
        return {"url": response.json()["secure_url"]}
    return {"error": response.text}

@app.post("/generate")
async def generate(data: Prompt):
    print("Received prompt:", data.prompt)
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(executor, generate_image_url_blocking, data.prompt)
    return result
