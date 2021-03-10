import socket
from Project_Screens import SampleApp
from Project_Canvas_Screen import CanvasScreen
import pickle

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
        # my_request = input("Please enter your request: ")


#         # serverSocket.send(my_request.encode())
#         # reply = serverSocket.recv(1024).decode()
#         #
#         # if reply == "OK":
#         #     client_canvas = CanvasScreen()
#         #     client_canvas.design_canvas_screen()
#         #     client_canvas.run_canvas()
#         #     while True:
#         #         if client_canvas.x_lst != [] and client_canvas.y_lst != []:
#         #             current_pos = (client_canvas.x_lst[-1], client_canvas.y_lst[-1])
#         #             serverSocket.send("re".encode())
#         #             serverSocket.send(pickle.dumps(current_pos))

        client_canvas = CanvasScreen()
        client_canvas.design_canvas_screen()
        client_canvas.run_canvas()
        while True:
            # if client_canvas.x_lst != [] and client_canvas.y_lst != []:
            #     current_pos = (client_canvas.x_lst[-1], client_canvas.y_lst[-1])
            #     print(current_pos)
            #     serverSocket.send("re".encode())
            #     serverSocket.send(pickle.dumps(current_pos))
            if client_canvas.positions_lst != []:
                current_pos = client_canvas.positions_lst[-1]
                serverSocket.send("re".encode())
                serverSocket.send(pickle.dumps(current_pos))


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1730
    c = Client(ip, port)
    c.start()