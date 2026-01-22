from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "HALCON OK"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json() or {}
    text = data.get("text", "")
    return jsonify({"answer": f"DUYDUM: {text}"})

if __name__ == "__main__":
    app.run()
