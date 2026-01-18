from flask import Flask, request, Response, jsonify

app = Flask(__name__)

command = None
output_buffer = []
finished = False

@app.route("/")
def health():
    return "CLI ↔ Colab Stream Relay (No Threads)"

@app.route("/send", methods=["POST"])
def send_command():
    global command, output_buffer, finished
    data = request.json
    cmd = data.get("command")

    if not cmd:
        return jsonify({"error": "No command"}), 400

    command = cmd
    output_buffer = []
    finished = False

    return jsonify({"status": "command accepted"})

@app.route("/fetch", methods=["GET"])
def fetch_command():
    global command
    if command:
        cmd = command
        command = None
        return jsonify({"command": cmd})
    return jsonify({"command": None})

@app.route("/push", methods=["POST"])
def push_output():
    global finished
    data = request.json
    line = data.get("line")

    if line is not None:
        output_buffer.append(line)

    if data.get("done"):
        finished = True

    return "OK"

@app.route("/stream")
def stream():
    def event_stream():
        idx = 0
        while True:
            while idx < len(output_buffer):
                yield f"data: {output_buffer[idx]}\n\n"
                idx += 1

            if finished:
                yield "data: [process finished]\n\n"
                break

    return Response(event_stream(), mimetype="text/event-stream")
