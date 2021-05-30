# Name: Shelly Rozman
# Python Version: 3.7.2
# Date: 14/3/2021
import multiprocessing
import random
import select
import threading
import time
from typing import List

from Project_Screens import Screens
import socket
import pickle


class Client(object):
    POSITION_LIST_LENGTH = 500

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start(self):
        """
        The function connects the client to a server's socket.
        """
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
        """
        The function starts the client's app screen.
        :param serverSocket: The server's socket.
        """
        app = Screens(serverSocket)
        # Communicate with server
        threading.Thread(target=self.send_and_recv_data, args=(app, serverSocket)).start()
        app.setup()

    def send_and_recv_data(self, app: Screens, server_socket):
        """
        The function sends a client's colored pixels positions list to the server,
        receives other clients' colored pixels positions list, and colors the pixels
        on the current client's canvas screen respectively.
        :param app: The client's canvas screen object.
        :param server_socket: The server's socket.
        """
        while app.running:
            data = pickle.dumps(app.positions_lst)
            app.positions_lst = []
            server_socket.send(data)

            # Receive the screen data from the server
            friend_screen = self.recv_data_in_chunks(server_socket)
            if friend_screen:
                # threading.Thread(target=self.draw_on_screen, args=(app, friend_screen, )).start()
                threading.Thread(target=app.color_pixel_for_server, args=(friend_screen,)).start()

    def recv_data_in_chunks(self, sock):
        """
        The function receives data from the server and loads it in chunks.
        :param sock: The server's socket.
        :return: The function returns the received data.
        :rtype: list.
        """
        BUFF_SIZE = 4096  # 4 KiB
        part = ""
        data = b''
        while True:
            part = sock.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                # either 0 or end of data
                break
        return pickle.loads(data)


