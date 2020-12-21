import tkinter as tk
from Project_Canvas_Screen import CanvasScreen
import socket
from Project_Screens import SampleApp

app = SampleApp()

class Client (object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start(self):
        try:
            print('connecting to ip %s port %s' % (ip, port))
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            print('connected to server')
            # send receive example
            msg = sock.recv(1024)
            print('received message: %s' % msg.decode())
            sock.sendall('Hello this is client, send me a job'.encode())
            #implement here your main logic
            while True:
                self.handleServerJob(sock)
        except socket.error as e:
            print(e)

    def handleServerJob(self, serverSocket):
        while True:
            my_request = input("Please enter your request: ")
            serverSocket.send(my_request.encode())
            reply = serverSocket.recv(1024).decode()
            print(reply)


            if reply == "SHOW":
                # canvas_obj = CanvasScreen()
                # canvas_obj.run_canvas()
                app.mainloop()



if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1730
    c = Client(ip, port)
    c.start()