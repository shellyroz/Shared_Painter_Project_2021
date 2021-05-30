import socket

from Project_Client import Client


def main():
    ip = socket.gethostbyname(socket.gethostname())
    # ip = '172.19.226.94'
    port = 1730
    c = Client(ip, port)
    c.start()


if __name__ == '__main__':
    main()
