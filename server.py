import socket

host = "localhost"
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12345))
server.listen(5)      
print("Bağlantı dinleniyor...")

client_socket,adres = server.accept()
file = open("server.jpg","wb")

image = client_socket.recv(102401)

while image:
    file.write(image)
    image = client_socket.recv(102401)

file.close()
client_socket.close()
