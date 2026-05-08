import socket

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("UDP sender pokrenut!")

broj_poruke = 1

while True:
    message = input(f"Message {broj_poruke}: ")

    sender.sendto(message.encode(), ("localhost", 12346))

    broj_poruke += 1

    if message.lower() == "exit":
        break

sender.close()