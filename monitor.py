import socket
import json

HOST = "127.0.0.1"
PORT = 6001

sock = socket.socket()
sock.connect((HOST, PORT))
print("[MONITOR] Bağlandı. Mesaj bekleniyor.\n")

buffer = ""
while True:
    veri = sock.recv(4096).decode()
    if not veri:
        break
    buffer += veri
    while "\n" in buffer:
        satir, buffer = buffer.split("\n", 1)
        if satir.strip():
            mesaj = json.loads(satir)
            print(f"  >>> [{mesaj['isim']}]: {mesaj['mesaj']}  (#{mesaj['sayi']})")