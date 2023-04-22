import socket


class ScreenClient:
    def __init__(self, host: str, port: int):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((host, port))
            self.client.send("hello".encode("utf-8"))
        except ConnectionRefusedError:
            self.client = None

    def get_screen(self, image_name: str):
        filename = f"./screens/{image_name}.jpg"
        with open(filename, 'wb') as image:
            data = self.client.recv(1024)
            while data:
                image.write(data)
                data = self.client.recv(1024)
        return filename
