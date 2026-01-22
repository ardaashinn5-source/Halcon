import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "HALCON aktif"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True)
    text = data.get("text", "")

    return jsonify({
        "answer": f"Seni duydum: {text}"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
