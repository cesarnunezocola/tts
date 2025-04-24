from flask import Flask, request, send_file
from TTS.api import TTS
import tempfile
import os

app = Flask(__name__)
tts = TTS(model_name="tts_models/es/css10/vits", progress_bar=False, gpu=False)

@app.route('/tts', methods=['POST'])
def tts_api():
    text = request.json.get("text", "")
    if not text:
        return {"error": "Texto vacío"}, 400

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as fp:
        tts.tts_to_file(text=text, file_path=fp.name)
        return send_file(fp.name, mimetype="audio/wav")

@app.route("/")
def index():
    return app.send_static_file("index.html")