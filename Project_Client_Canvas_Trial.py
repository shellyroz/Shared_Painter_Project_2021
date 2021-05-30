import random
import threading
import time
import tkinter as tk
# from Project_Canvas_Screen import CanvasScreen
from select import select

from Updated_Project_Canvas_Screen1 import CanvasScreen1
from New_Updated_Project_Canvas_Screen import CanvasScreen
from concurrent.futures import Executor
import socket
import pickle
import sys
# from Project_Screens import SampleApp
#
# app = SampleApp()

class Client1(object):
    POSITION_LIST_LENGTH = 500

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start(self):
        '''
        The function connects the client to a server's socket.
        '''
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
        '''
        The function starts the client's app screen.
        :param serverSocket: The server's socket.
        '''
        # can_start = serverSocket.recv(1024).decode()
        # if can_start == "START":
        app = CanvasScreen()
        # app.design_initial_screen()
        # Communicate with server
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
        '''
        The function sends a client's colored pixels positions list to the server,
        receives other clients' colored pixels positions list, and colors the pixels
        on the current client's canvas screen respectively.
        :param app: The client's canvas screen object.
        :param server_socket: The server's socket.
        '''
        while app.running:
            data = pickle.dumps(app.positions_lst)

            for elem in app.positions_lst:
                print("sent: ")
                print(elem[1])

            server_socket.send(data)
            app.positions_lst = []

            # Receive the screen data from the server
            friend_screen = self.recv_data_in_chunks(server_socket)
            threading.Thread(target=self.draw_on_screen, args=(app, friend_screen, )).start()

    def draw_on_screen(self, app, friend_screen):
        '''
        The function colors pixels on the clients canvas screen respectively to other client's drawings.
        :param app: The client's canvas screen object.
        :param friend_screen: A list of another client's colored pixels positions.
        '''
        # Draw all pixels on the screen1
        for pixel in friend_screen:
            color = pixel[0]
            coord = pixel[1]
            print("received: ")
            print(coord)
            x, y = coord[0], coord[1]
            brush_size = pixel[2]
            brush_type = pixel[3]

            if brush_type == "●":
                for i in range(x, x + brush_size):
                    for j in range(y, y + brush_size):
                        if x >= 0:
                            app.color_pixel_for_server((i, j), color)

            elif brush_type == "*":
                for i in range(brush_size):
                    pixels_to_color = [(x, y), (x + i, y), (x + i, y + i), (x, y + i), (x - i, y), (x - i, y - i),
                                       (x, y - i)]
                    # Eliminate repetitions
                    pixels_to_color = list(set(pixels_to_color))
                    # Color and append to the positions list every pixel in the list
                    for pixel in pixels_to_color:
                        if x >= 0:
                            app.color_pixel_for_server(pixel, color)


    def draw_on_screen1(self, app, friend_screen):
        # Draw all pixels on the screen1
        for pixel in friend_screen:
            app.color_pixel_for_server(pixel[1], pixel[0])
            #threading.Thread(target=app.color_pixel_for_server, args=(pixel[1], pixel[0],)).start()

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
        '''
        The function receives data from the server and loads it in chunks.
        :param sock: The server's socket.
        :return: The function returns the received data.
        :rtype: list.
        '''
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