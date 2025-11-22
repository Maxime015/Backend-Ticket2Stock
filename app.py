import easyocr
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from modules.OcrModule import OcrModule
import base64, binascii

app = Flask(__name__)
CORS(app)

@app.route("/scan", methods=['POST', 'GET'])
def load_ticket():
    content = request.get_json()
    base64_string = content.get('base64String')
    image = base64.b64decode(base64_string, validate=True)
    ocr = OcrModule()
    ocr.extract_data_from_ticket(image)
    result = ocr.formatToJson()
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)