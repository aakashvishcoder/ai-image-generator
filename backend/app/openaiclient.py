import openaiclient
import os

openai.api_key = os.getenv("")

async def generate_image(prompt: str):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return {"url":response["data"][0]["url"]}
