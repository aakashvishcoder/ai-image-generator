import os
import replicate
from dotenv import load_dotenv

load_dotenv()

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
client = replicate.Client(api_token=REPLICATE_API_TOKEN)

def generate_image(prompt: str):
    model_id = "ultralytics/yolo11n" #change this a different replicate model
    try:
        output_urls = client.run(
            model_id,
            input={"prompt": prompt}
        )
        print("Replicate output:", output_urls)  
        if output_urls:
            return {"url": output_urls[0]}
        else:
            return {"error": "No image generated"}
    except replicate.exceptions.ReplicateError as e:
        print(f"Replicate API error: {e}")
        return {"error": f"Replicate API error: {e}"}

