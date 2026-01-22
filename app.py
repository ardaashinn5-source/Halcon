from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "HALCON aktif"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"answer": "Bir şey duyamadım"}), 400

    return jsonify({
        "answer": f"Seni duydum. '{text}' dedin."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
