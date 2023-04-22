import socket
from PIL import ImageGrab

port = 2000  # change port if needed
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", port))
server.listen(1)

while True:
    client_socket, address = server.accept()
    request = client_socket.recv(1024)
    image = ImageGrab.grab()
    image.save('buffer.png')
    with open('buffer.png', 'rb') as data:
        data_part = data.read(1024)
        while data_part:
            client_socket.send(data_part)
            data_part = data.read(1024)
    client_socket.close()
