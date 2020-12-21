import tkinter as tk
from Project_Canvas_Screen import CanvasScreen
import socket
import threading

class Server(object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.count = 0

    def start(self):
        try:
           print('server starts up on ip %s port %s' % (self.ip, self.port))
           # Create a TCP/IP socket
           sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           sock.bind((self.ip, self.port))
           sock.listen(3)

           while True:
                print('waiting for a new client')
                # block
                clientSocket, client_address = sock.accept()

                print('new client entered')

                # send receive example
                clientSocket.sendall('Hello this is server'.encode())
                msg = clientSocket.recv(1024)
                print('received message: %s' % msg.decode())
                self.count += 1
                print(self.count)
                # implement here your main logic
                self.handleClient(clientSocket, self.count)
        except socket.error as e:
            print(e)

    def handleClient(self, clientSock, current):
        print ("hello")
        client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current,))
        # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
        client_handler.start()

    def handle_client_connection(self, client_socket, current):
         while True:
            print("start")
            request = client_socket.recv(1024).decode()
            print(request)


            if request == "SCRN":
                client_socket.sendall(str("SHOW").encode())


         client_socket.close()



if __name__ == '__main__':
   ip = '0.0.0.0'
   port = 1730
   s = Server(ip, port)
   s.start()