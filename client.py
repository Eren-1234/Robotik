import socket                

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect("localhost", 12345)

file = open("resim.jpg","rb")

image_data = file.read(102401)

while image_data:
    client.send(image_data)
    image_data = file.read(102401)

file.close()
client.close()