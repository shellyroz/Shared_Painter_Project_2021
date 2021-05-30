'''3.12-1.4-6.4-5.5-4.2'''
import tkinter as tk
from select import select

from Project_Canvas_Screen import CanvasScreen
import socket
import threading
import pickle
import sys
from sign_up_database1 import Users
from login_database1 import Users1
from Project_Email_Handle import EmailBot
import hashlib
# from Hash_Encryption_Trial import Encryption


class Server1(object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.clients_lst = []
        self.clients_and_screen = {}
        self.game_screen = []
        self.count = 0
        self.sign_up_database = Users()
        self.login_database = Users1()
        self.email_sender = EmailBot()
        #self.e = Encryption()


    def encrypt(self, password):
        '''
        The function encrypts a given password.
        :param password: A given password.
        '''
        return hashlib.sha256(password.encode()).hexdigest()

    def sign_up(self, entry1, entry2, entry3):
        '''
        The function which logs a new client's sign up information into
        the designated sign up database.
        :param entry1: The new client's entered email.
        :param entry2: The new client's entered username.
        :param entry3: The new client's entered password.
        '''
        encrypted_password = self.encrypt(entry3)
        self.sign_up_database.insert_user(entry1, entry2, encrypted_password)
        self.sign_up_database.create_users_list()


    def login(self, entry2, entry3):
        '''
        The function which logs a client's login information into
        the designated login database.
        :param entry2: The client's entered username.
        :param entry3: The client's entered password.
        '''
        encrypted_password = self.encrypt(entry3)
        self.login_database.insert_user(entry2, encrypted_password)
        self.login_database.create_users_list()
        self.sign_up_database.create_users_list()

        rtrn = self.sign_up_database.is_user_in_database(entry2, encrypted_password)

        print(rtrn)

        if "ERROR" not in rtrn:
            # self.login_frame.pack_forget()
            users_email = rtrn
            self.email_sender.send_email(users_email)
            # self.login_code_screen(self.email_sender.code)
            print("given code is: " + self.email_sender.code)
            return "ok"


        elif rtrn == "U_ERROR" or rtrn == "P_ERROR":
            return "not ok"
            print(rtrn)


    def is_login_code_ok(self, code_entry):
        '''
        The function checks whether the client's entered login code is correct or not.
        :param code_entry: The client's code entry.
        :return: True if the entered code is correct, and False if it is incorrect.
        :rtype: bool.
        '''
        entered_code = code_entry.get()
        print("entered code is: " + entered_code)

        return entered_code == self.email_sender.code


    def check_to_change_password(self, entered_username):
        '''
        The function checks whether the client's entered username exists in the
        sign up database or not.
        :param entered_username: The client's entered username.
        :return: True if the client's entered username exists in the
        sign up database, and False if it does not.
        :rtype: bool.
        '''
        self.sign_up_database.create_users_list()
        print(entered_username)
        can_change_password = self.sign_up_database.is_username_in_database(entered_username)
        print(can_change_password)

        return can_change_password

    def change_to_new_password(self, entered_username, new_password):
        '''
        The function changes the client's password to an entered new password.
        :param entered_username: The client's entered username.
        :param new_password: The client's entered password.
        '''
        encrypted_new_password = self.encrypt(new_password)
        self.sign_up_database.change_password(entered_username, encrypted_new_password)
        # self.sign_up_database.create_users_list()
        # print(self.sign_up_database.users_list)

    def start(self):
        '''
        The function connects clients to the server.
        '''
        try:
            print('server starts up on ip %s port %s' % (self.ip, self.port))
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self.ip, self.port))
            sock.listen(5)
            while True:
                client, addr = sock.accept()
                self.clients_lst.append(client)
                client.send("#cybercyber".encode())
                self.handleClient(client)
        except socket.error as e:
            print(e)

    def read_from_clients(self, read_list):
        """Add every client's screen to the game screen"""
        for client in read_list:
            data = self.recv_data_in_chunks(client)
            for client2 in self.clients_lst:
                if client2 != client:
                    self.clients_and_screen[client2] += data

    def write_to_clients(self, write_list):
        """Send every client the game screen"""
        for client in write_list:
            client.send(pickle.dumps(self.clients_and_screen[client]))
            self.clients_and_screen[client] = []

    def connect_clients(self, sock):
        while True:
            client, addr = sock.accept()
            self.clients_lst.append(client)
            self.clients_and_screen[client] = []
            print(addr)
            client.send("hello this is server speaking".encode())


    def handleClient(self, clientSock):
        '''
        The function handles client connections.
        :param clientSock: The current client's socket.
        '''
        print("hello")
        client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock,))
        # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
        client_handler.start()

    def handle_client_connection(self, client_socket):
        '''
        The function sends data from the server to all clients connected to the server,
        except from the client that sent the data.
        :param client_socket: The socket of the client who sent the data.
        '''
        # print("start")
        # client_socket.sendall(str("START").encode())
        # pos_lst_size = pickle.loads(client_socket.recv(25600)) * 8 # Size is in bytes. Thus, we need to convert to bits.
        # print(pos_lst_size)
        # pos_lst = pickle.loads(client_socket.recv(pos_lst_size))
        #
        # print(pos_lst)

        # positions_lst = []
        # client_socket.sendall(pickle.dumps(lst_to_receive_len))

        # while True:
        #     data = pickle.loads(client_socket.recv(25600))
        #     print(data)
        #     client_socket.sendall(pickle.dumps(data))
        #     if not data:
        #         print("ERROR")

        # for client in self.clients_lst:
        #     this_client_socket = client
        #     if this_client_socket != client_socket:
        #         this_client_socket.sendall(pickle.dumps(lst_to_receive_len))
        #
        # for i in range(lst_to_receive_len):
        #     position = pickle.loads(client_socket.recv(25600))
        #     # client_socket.sendall(pickle.dumps(position))
        #     # positions_lst.append(position)
        #     for client in self.clients_lst:
        #         this_client_socket = client
        #         this_client_socket.send(pickle.dumps(position))
        # lst_to_receive_len = pickle.loads(client_socket.recv(1024))

        while True:
            data = self.recv_data_in_chunks(client_socket)
            for client in self.clients_lst:
                if client is client_socket:
                    continue
                # do_something = threading.Thread(target=client.send(position), args=(client_socket, current,))
                # do_something.start()
                client.send(pickle.dumps(data))

    def recv_data_in_chunks(self, sock):
        '''
        The function receives data from the client and loads it in chunks.
        :param sock: The client's socket.
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



if __name__ == '__main__':
   ip = '192.168.1.35'
   # ip = '172.19.225.89'
   port = 1730
   s = Server1(ip, port)
   s.start()