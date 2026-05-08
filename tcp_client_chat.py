import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 2004))

print("Povezan na server (port 2004)")

broj_poruke = 1

while True:
    msg = input("Unesi poruku (exit za kraj): ")

    client.send(msg.encode())

    if msg.lower() == "exit":
        break

    odgovor = client.recv(1024).decode()
    print("Server kaže:", odgovor)

client.close()