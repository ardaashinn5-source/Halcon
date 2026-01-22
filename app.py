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

    answer = response.choices[0].message.content
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
