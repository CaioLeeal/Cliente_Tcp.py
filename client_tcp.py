import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("google.com",80))
client.send(b"GET / HTTP/1.1 \nHOST: www.google.com\n\n\n")
pacotes = client.recv(1024)
print(pacotes)