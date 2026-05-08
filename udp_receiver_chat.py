import socket

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

receiver.bind(("localhost", 12346))

print("UDP receiver čeka poruke na portu 12346...")

broj_poruke = 1

while True:
    data, addr = receiver.recvfrom(1024)

    message = data.decode()

    print(f"Message {broj_poruke}: {message}")

    broj_poruke += 1

    if message.lower() == "exit":
        break

receiver.close()