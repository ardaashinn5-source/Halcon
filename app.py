from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "HALCON aktif"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"answer": "Bir şey duyamadım."})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sen HALCON adında Türkçe konuşan bir yapay zeka asistansın."},
            {"role": "user", "content": text}
        ]
    )

    answer = response.choices[0].message.content
    return jsonify({"answer": answer})

