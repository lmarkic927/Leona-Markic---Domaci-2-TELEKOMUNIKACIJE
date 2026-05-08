import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 2004))
server.listen(1)

print("Server čeka konekciju na portu 2004...")

conn, addr = server.accept()
print("Povezan sa:", addr)

broj_poruke = 1

while True:
    data = conn.recv(1024)

    if not data:
        break

    msg = data.decode()

    print(f"Message {broj_poruke}: {msg}")
    broj_poruke += 1

    conn.send("ACK".encode())

    if msg.lower() == "exit":
        break

conn.close()
server.close()