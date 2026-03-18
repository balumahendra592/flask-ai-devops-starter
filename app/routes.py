from flask import Blueprint, request, jsonify
from .ai import ask_ai

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return jsonify({"status": "ok", "message": "Flask AI DevOps Starter is running 🚀"})

@main.route("/health")
def health():
    return jsonify({"status": "healthy"})

@main.route("/ai/ask", methods=["POST"])
def ai_ask():
    data = request.get_json()
    if not data or "prompt" not in data:
        return jsonify({"error": "Missing 'prompt' in request body"}), 400

    response = ask_ai(data["prompt"])
    return jsonify({"response": response})
