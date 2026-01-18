import requests
import sys

SERVER = "https://skyreels-v2-magic-access.onrender.com/"

cmd = " ".join(sys.argv[1:])
if not cmd:
    print("Usage: cli.py <command>")
    sys.exit(1)

requests.post(f"{SERVER}/send", json={"command": cmd})

with requests.get(f"{SERVER}/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
