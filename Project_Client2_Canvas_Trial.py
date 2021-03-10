import threading
import tkinter as tk
# from Project_Canvas_Screen import CanvasScreen
from Updated_Project_Canvas_Screen import CanvasScreen
import socket
import pickle
import sys
# from Project_Screens import SampleApp
#
# app = SampleApp()

class Client(object):

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
            self.handleServerJob(sock)
        except socket.error as e:
            print(e)

    def handleServerJob(self, serverSocket):
        # can_start = serverSocket.recv(1024).decode()
        # if can_start == "START":
        app = CanvasScreen()
        # app.design_initial_screen()
        threading.Thread(target=self.gambit, args=(app, serverSocket)).start()
        app.setup()
        # print(sys.getsizeof(app.positions_lst))
        # lst_to_send_size = sys.getsizeof(app.positions_lst) *

            # pos_to_recv = pickle.loads(serverSocket.recv(25600))
            # print(pos_to_recv)

            # serverSocket.send(pickle.dumps(lst_to_send_size))
            # serverSocket.send(pickle.dumps(lst_to_send))

            # lstlst = pickle.loads(serverSocket.recv(25600).decode())
            # print(lstlst)

    def gambit(self, app: CanvasScreen, serverSocket):
        while app.running:
            lst_to_send = app.positions_lst

            # data = pickle.dumps(lst_to_send)
            # serverSocket.send(pickle.dumps(lst_to_send_len))

            # for i in range(0, len(data), 1024):
            # serverSocket.send(data)
            # print(pickle.loads(serverSocket.recv(25600)))

            serverSocket.send(pickle.dumps(lst_to_send))
            if app.positions_lst:
                print(app.positions_lst)
            try:
                screen = pickle.loads(serverSocket.recv(25600))
            except Exception as e:
                screen = []
            for pixel in screen:
                app.color_pixel_for_server(app.photo, pixel[1], pixel[0])

        # while True:
        #     can_start = serverSocket.recv(1024).decode()
        #     if can_start == "START":
        #         app = CanvasScreen()
        #         app.design_initial_screen()

            # my_request = input("Please enter your request: ")
            # serverSocket.send(my_request.encode())
            # reply = serverSocket.recv(1024).decode()
            # print(reply)
            #
            #
            # if reply == "SHOW":
            #     app = CanvasScreen()
            #     app.design_initial_screen()
            #
            # print(app.is_login_pressed)
            # if app.is_login_pressed:
            #     serverSocket.send("LOGN".encode())
            # logn = serverSocket.recv(1024).decode()
            # print(logn)
        #         # canvas_obj = CanvasScreen()
        #         # canvas_obj.run_canvas()
        #         app.mainloop()




if __name__ == '__main__':
    ip = '192.168.1.33'
    port = 1730
    c = Client(ip, port)
    c.start()