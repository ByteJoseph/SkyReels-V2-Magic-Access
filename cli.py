import requests, time

SERVER = "https://skyreels-v2-magic-access.onrender.com/"

while True:
    cmd = input("colab> ").strip()
    if not cmd:
        continue

    requests.post(f"{SERVER}/send", json={"command": cmd})

    while True:
        r = requests.get(f"{SERVER}/result").json()
        if r["output"]:
            print(r["output"])
            break
        time.sleep(1)
