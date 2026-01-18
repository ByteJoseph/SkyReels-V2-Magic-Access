from flask import Flask, request, jsonify
from collections import deque

app = Flask(__name__)

# In-memory queues (OK for MVP; use Redis later)
command_queue = deque()
result_queue = deque()

@app.route("/")
def health():
    return "CLI ↔ Colab Relay Running"

@app.route("/send", methods=["POST"])
def send_command():
    data = request.json
    command = data.get("command")

    if not command:
        return jsonify({"error": "No command provided"}), 400

    command_queue.append(command)
    return jsonify({"status": "command queued"})

@app.route("/fetch", methods=["GET"])
def fetch_command():
    if command_queue:
        return jsonify({"command": command_queue.popleft()})
    return jsonify({"command": None})

@app.route("/result", methods=["POST"])
def post_result():
    data = request.json
    output = data.get("output")

    if not output:
        return jsonify({"error": "No output provided"}), 400

    result_queue.append(output)
    return jsonify({"status": "result stored"})

@app.route("/result", methods=["GET"])
def fetch_result():
    if result_queue:
        return jsonify({"output": result_queue.popleft()})
    return jsonify({"output": None})


