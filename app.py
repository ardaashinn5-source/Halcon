import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "HALCON aktif"

from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True)
    user_text = data.get("text", "")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sen Türkçe konuşan, yardımcı bir yapay zeka asistanısın. Adın HALCON."},
            {"role": "user", "content": user_text}
        ]
    )

    answer = response.choices[0].message.content

    return jsonify({"answer": answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
