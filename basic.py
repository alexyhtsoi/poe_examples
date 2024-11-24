import fastapi_poe as fp
import modal
from typing import Callable
from modal import App, Image, asgi_app
from fastapi import Request

app = modal.App()

@modal.web_endpoint()
async def basic_endpoint(request: Request):
    # Parse the JSON body from the request
    data = await request.json()
    # Echo back the received message
    return {"message": f"Hello, you said: {data.get('message', 'nothing')}"}

# curl -X POST https://modal.com/apps/alexyhtsoi/main/ap-ADdWObu2kqyTLiGOePU1x6 \
# -H "Content-Type: application/json" \
# -d '{"message": "Hello, Modal!"}'