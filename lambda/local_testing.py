from flask import Flask, request, jsonify, Response
from handler import handler
import base64
import json

app = Flask(__name__)

@app.route("/resize", methods=["GET"])
def resize():
    event = {
        "queryStringParameters": {
            "url": request.args.get("url"),
            "width": request.args.get("width"),
            "height": request.args.get("height")
        }
    }
    result = handler(event, None)
    status = result.get("statusCode", 500)

    if result.get("isBase64Encoded") and status == 200:
        image_bytes = base64.b64decode(result["body"])
        return Response(image_bytes, status=status, mimetype="image/png")
    else:
        body = result.get("body")
        if isinstance(body, str):
            try:
                body = json.loads(body)
            except Exception:
                body = {"error": body}
        return jsonify(body), status

if __name__ == "__main__":
    app.run(debug=True)
