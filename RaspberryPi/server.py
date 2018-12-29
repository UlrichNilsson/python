#!/usr/bin/env python3

import socket
import sys

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    mysock.bind(("",80))
except socket.error:
    print("Failed to bind")
    sys.exit()
mysock.listen(5)
while True:
    conn, addr = mysock.accept()
    data = conn.recv(1000)
    if not data:
        break
    conn.sendall(b'Got a request!')
    print("Got a request!")
conn.close()
mysock.close()

