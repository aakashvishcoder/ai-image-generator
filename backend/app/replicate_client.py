import os
import io
import requests
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load secrets from .env
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")  
CLOUDINARY_UPLOAD_URL = os.getenv("CLOUDINARY_UPLOAD_URL")  # full upload URL from Cloudinary dashboard

hf_client = InferenceClient(provider="fal-ai", api_key=HF_API_KEY)

def generate_image_url(prompt: str):
    image = hf_client.text_to_image(prompt, model="Qwen/Qwen-Image")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    response = requests.post(CLOUDINARY_UPLOAD_URL, files={"file": buffer})
    if response.status_code == 200:
        return {"url": response.json()["secure_url"]}
    return {"error": response.text}
