from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "HALCON aktif"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_text = data.get("text", "")

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "Sen HALCON adında, Türkçe konuşan bir yapay zeka asistansın."},
            {"role": "user", "content": user_text}
        ]
    )

    return jsonify({"answer": response.choices[0].message.content})
