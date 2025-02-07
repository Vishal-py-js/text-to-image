from celery import shared_task
import base64
import os
import requests

engine_id = "stable-diffusion-v1-6"
api_host = os.getenv('API_HOST')
api_key = os.getenv("API_KEY")

@shared_task
def async_generator(prompt):
    if api_key is None:
        raise Exception("Missing Stability API key.")
    
    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": prompt
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )
    
    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for i, image in enumerate(data["artifacts"]):
        imgdata = base64.b64decode(image["base64"])
        return imgdata