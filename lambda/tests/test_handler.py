import io
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from PIL import Image
from handler import handler

class DummyResponse:
    def __init__(self, content):
        self.content = content

def make_test_image_bytes():
    buf = io.BytesIO()
    Image.new('RGB', (10,10), color='blue').save(buf, format='PNG')
    return buf.getvalue()

def test_resize_success(monkeypatch):
    # Mock requests.get to return our test image
    img_bytes = make_test_image_bytes()
    monkeypatch.setattr("handler.requests.get", lambda url: DummyResponse(img_bytes))

    event = {"queryStringParameters": {"url": "http://x", "width": "5", "height": "5"}}
    result = handler(event, None)

    assert result["statusCode"] == 200
    assert result["isBase64Encoded"] is True

def test_missing_params():
    result = handler({"queryStringParameters": {}}, None)
    assert result["statusCode"] == 400
