# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.openai_client import OpenAIClient

app = Flask(__name__)

# 🔥 FULL CORS FIX — works with React, Vite, Chrome, Safari
CORS(app, resources={r"/*": {"origins": "*"}})

client = OpenAIClient()


@app.route("/")
def home():
    return jsonify({
        "message": "StudyFlow backend running on port 5000"
    })


# ✅ MATCHES FRONTEND EXACTLY
# fetch("http://localhost:5000/api/generate")
@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json()

    # 🔥 FRONTEND SENDS "text", NOT "prompt"
    text = data.get("text")
    mode = data.get("mode", "full")

    if not text:
        return jsonify({"error": "Text is required"}), 400

    # 🔥 AI call
    output = client.generate_text(text, mode)

    # 🔥 FRONTEND EXPECTS "notes"
    return jsonify({
        "notes": output
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
