# Name: Shelly Rozman
# Python Version: 3.7.2
# Date: 30/05/2021
import socket
from Project_Server import Server


def main():
    ip = socket.gethostbyname(socket.gethostname())
    #ip = '172.19.226.94'
    port = 1730
    s = Server(ip, port)
    s.start()


if __name__ == '__main__':
    main()