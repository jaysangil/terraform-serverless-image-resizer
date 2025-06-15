import json
import os
import requests
import base64
from io import BytesIO
from PIL import Image

def handler(event, context):
    params = event.get("queryStringParameters") or {}
    url    = params.get("url")
    w      = int(params.get("width", 0))
    h      = int(params.get("height", 0))

    if not url or w <= 0 or h <= 0:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Missing or invalid parameters"})
        }

    resp = requests.get(url)
    img  = Image.open(BytesIO(resp.content))
    img  = img.resize((w, h))

    buf = BytesIO()
    img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode()

    return {
        "statusCode":      200,
        "headers":         {"Content-Type": "image/png"},
        "body":            b64,
        "isBase64Encoded": True
    }
