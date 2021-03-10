import threading
import tkinter as tk
# from Project_Canvas_Screen import CanvasScreen
from select import select

from Updated_Project_Canvas_Screen import CanvasScreen
import socket
import pickle
import sys
# from Project_Screens import SampleApp
#
# app = SampleApp()

class Client(object):
    POSITION_LIST_LENGTH = 500

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start(self):
        try:
            print('connecting to ip %s port %s' % (self.ip, self.port))
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.ip, self.port))
            print('connected to server')
            # send receive example
            msg = sock.recv(1024)
            print('received message: %s' % msg.decode())
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

    def gambit(self, app: CanvasScreen, server_socket):
        while app.running:
            data = pickle.dumps(app.positions_lst)

            server_socket.send(data)
            app.positions_lst = []

            # Receive the screen data from the server
            screen = self.recv_data_in_chunks(server_socket)

            # Draw all pixels on the screen
            for pixel in screen:
                app.color_pixel_for_server(app.photo, pixel[1], pixel[0])

    def read_from_server(self, read_list, app):
        for sock in read_list:
            screen = pickle.loads(self.recv_data_in_chunks(sock))
            for pixel in screen:
                app.color_pixel_for_server(app.photo, pixel[1], pixel[0])

    def write_to_server(self, write_list, app):
        for sock in write_list:
            data = pickle.dumps(app.positions_lst)

            sock.send(data)
            app.positions_lst = []

    def recv_data_in_chunks(self, sock):
            BUFF_SIZE = 4096  # 4 KiB
            data = b''
            while True:
                part = sock.recv(BUFF_SIZE)
                data += part
                if len(part) < BUFF_SIZE:
                    # either 0 or end of data
                    break
            return pickle.loads(data)

    def recv_data_in_chunks1(self, client_socket):
        return pickle.loads(client_socket.recv(25600))
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




# if __name__ == '__main__':
#     ip = '192.168.1.33'
#     port = 1730
#     c = Client(ip, port)
#     c.start()