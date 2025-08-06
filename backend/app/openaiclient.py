import openai
import os
from dotenv import load_dotenv

load_dotenv()  # load from .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise Exception("OPENAI_API_KEY not set")

# async def generate_image(prompt: str):
#     response = openai.Image.create(
#         prompt=prompt,
#         n=1,
#         size="512x512"
#     )
#     return {"url": response["data"][0]["url"]}

async def generate_image(prompt: str):
    # Mocked response to simulate an image URL
    return {"url": "https://via.placeholder.com/512?text=Mock+Image"}
