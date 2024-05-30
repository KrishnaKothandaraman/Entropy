import socket
import json

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("localhost", 5001))

while True:
    msgString = input("Enter json: ")
    if msgString == 'die':
        break

    msg = json.dumps(
        json.loads(msgString)).encode("utf-8")

    c.sendall(msg)