"""3.12-1.4-6.4-5.5-4.2"""
# Name: Shelly Rozman
# Python Version: 3.7.2
# Date: 14/3/2021
import multiprocessing
import socket
import threading
import pickle
from select import select

from Sign_Up_Database import SignedUpUsers
from Login_Database import LoggedInUsers
from Project_Email_Handle import EmailBot
import hashlib
import sqlite3
import tkinter as tk
import tkinter.messagebox
import glob


class Server(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.clients_lst = [None]
        self.clients_and_screen = {}
        self.cur_game_screen = []
        self.game_screen = []
        self.count = 0
        self.sign_up_database = SignedUpUsers()
        self.login_database = LoggedInUsers()
        self.email_sender = EmailBot()
        self.screenshot_num = 0

    def encrypt(self, password):
        """
        The function encrypts a given password.
        :param password: A given password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def sign_up(self, entered_email, entered_username, entered_password):
        """
        The function which logs a new client's sign up information into
        the designated sign up database.
        :param entered_email: The new client's entered email.
        :param entered_username: The new client's entered username.
        :param entered_password: The new client's entered password.
        """
        encrypted_password = self.encrypt(entered_password)
        try:
            self.sign_up_database.insert_user(entered_email, entered_username, encrypted_password)
            return "success"
        except sqlite3.IntegrityError:
            tk.Tk().withdraw()
            tk.messagebox.showerror(title="ERROR",
                                    message="The username '" + entered_username + "' is unavailable. "
                                                                         "Please enter a different username.")
            return "error"
        self.sign_up_database.create_users_list()


    def login(self, entered_username, entered_password):
        """
        The function which logs a client's login information into
        the designated login database.
        :param entered_username: The client's entered username.
        :param entered_password: The client's entered password.
        """
        encrypted_password = self.encrypt(entered_password)

        self.sign_up_database.create_users_list()
        self.login_database.create_users_list()
        print(self.login_database.users_list)

        rtrn = self.sign_up_database.is_user_in_database(entered_username, encrypted_password)

        print(rtrn)

        rtrn1 = self.login_database.is_username_in_database(entered_username)

        print(rtrn1)


        if "ERROR" not in rtrn and rtrn1 == False:
            self.login_database.insert_user(entered_username, encrypted_password)
            self.login_database.create_users_list()
            # self.login_frame.pack_forget()
            users_email = rtrn
            self.email_sender.send_code_email(users_email)
            # self.login_code_screen(self.email_sender.code)
            print("given code is: " + self.email_sender.code)
            return "ok"

        elif rtrn1:
            tk.Tk().withdraw()
            tk.messagebox.showerror(title="ERROR",
                                    message="You are already logged in. Please log in from a different user.")
            return "not ok"

        elif rtrn == "U_ERROR" or rtrn == "P_ERROR":
            return "not ok"
            print(rtrn)


    def is_login_code_ok(self, code_entry):
        """
        The function checks whether the client's entered login code is correct or not.
        :param code_entry: The client's code entry.
        :return: True if the entered code is correct, and False if it is incorrect.
        :rtype: bool.
        """
        entered_code = code_entry.get()
        print("entered code is: " + entered_code)

        return entered_code == self.email_sender.code

    def check_to_change_password(self, entered_username):
        """
        The function checks whether the client's entered username exists in the
        sign up database or not.
        :param entered_username: The client's entered username.
        :return: True if the client's entered username exists in the
        sign up database, and False if it does not.
        :rtype: bool.
        """
        self.sign_up_database.create_users_list()
        print(entered_username)
        can_change_password = self.sign_up_database.is_username_in_database(entered_username)
        print(can_change_password)

        return can_change_password

    def change_to_new_password(self, entered_username, new_password):
        """
        The function changes the client's password to an entered new password.
        :param entered_username: The client's entered username.
        :param new_password: The client's entered password.
        """
        encrypted_new_password = self.encrypt(new_password)
        self.sign_up_database.change_password(entered_username, encrypted_new_password)

    def delete_login(self, username):
        """
        The function deletes a given client from the login database.
        :param username: The given client's username.
        """
        self.login_database.delete_user(username)

    def update_screenshot_num(self):
        """
        The function updates the serial number of a saved screenshot.
        """
        for filename in glob.glob(r'Cropped_Screenshots/*.png'):  # assuming png
            with open(filename, "rb") as f:
                file_name = f.name
                file_name = file_name.replace(".png", "")
                file_str_arr = file_name.split("_")
                file_num = file_str_arr[-1]
                if int(file_num) > int(self.screenshot_num):
                    self.screenshot_num = file_num


    def send_saved_screenshot(self, given_username, img_path):
        """
        The function sends a saved screenshot to the client who saved it.
        :param given_username: The username of the client who saved the screenshot.
        :param img_path: The screenshot's path.
        """
        rtrn = self.sign_up_database.email_by_username(given_username)

        if rtrn != "ERROR":
            users_email = rtrn
            self.email_sender.send_screenshot_email(users_email, img_path)
            print("Screenshot sent :)")


    # def delete_table(self):
    #     self.login_database.delete_table()

    # def start1(self):
    #     threading.Thread(target=self.connect_clients).start()
    #     while True:
    #         if not self.clients_lst:
    #             continue
    #         read_list, write_list, nothing = select(self.clients_lst, self.clients_lst, [])
    #         self.handle_read(read_list)
    #         self.handle_write(write_list)
    #
    # def handle_read(self, read_list):
    #     for client in read_list:
    #         data = self.recv_data_in_chunks(client)
    #         self.cur_game_screen += data
    #
    # def handle_write(self, write_list):
    #     if not self.cur_game_screen:
    #         return
    #     for client in write_list:
    #         client.send(pickle.dumps(self.cur_game_screen))
    #     self.cur_game_screen = []

    def connect_clients(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.ip, self.port))
        sock.listen(1)
        while True:
            client, addr = sock.accept()
            self.clients_lst[0] = client
            client.send("#cybercyber".encode())

    def start(self):
        """
        The function connects clients to the server and handles their connections.
        """
        try:
            threading.Thread(target=self.handle_client).start()
            print('server starts up on ip %s port %s' % (self.ip, self.port))
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self.ip, self.port))
            sock.listen(1)
            while True:
                client, addr = sock.accept()
                self.clients_lst[0] = client
                client.send("#cybercyber".encode())
                #self.handleClient(client)
        except socket.error as e:
            print(e)

    # def handleClient(self, clientSock):
    #     """
    #     The function handles client connections.
    #     :param clientSock: The current client's socket.
    #     """
    #     print("hello")
    #     client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock,))
    #     client_handler.start()

    '''def handle_client_connection(self, client_socket):
        """
        The function sends data from the server to all clients connected to the server,
        except from the client that sent the data.
        :param client_socket: The socket of the client who sent the data.
        """
        while True:
            data = self.recv_data_in_chunks(client_socket)
            for client in self.clients_lst:
                if client is client_socket:
                    continue
                client.send(pickle.dumps(data))'''

    def handle_client(self):
        """
        The function receives data from one client and
        sends it to all the other clients connected to the system.
        """
        while True:
            if len(self.clients_lst) == 1 and not self.clients_lst[0]:
                continue
            no_new_client = self.clients_lst[0] is None
            for client in self.clients_lst[int(no_new_client):]:
                self.read_from_client(client)
            for client in self.clients_lst[1:]:
                self.write_to_client(client, self.cur_game_screen)
            if not no_new_client:
                self.write_to_client(self.clients_lst[0], self.game_screen)
                self.clients_lst.insert(0, None)
            self.cur_game_screen = []



    def read_from_client(self, client):
        """
        The function receives data from the client.
        :param client: The client's socket.
        """
        data = self.recv_data_in_chunks(client)

        if data and data[0] == "disconnect":
            self.disconnect_client(client)
        else:
            self.cur_game_screen += data
            self.game_screen += data
        # if ("disconnect") in data:
        #     self.disconnect_client(client)
        # else:
        #     self.cur_game_screen += data
        #     self.game_screen += data

    def write_to_client(self, client, screen):
        """
        The function sends data to the client.
        :param client: The client's socket.
        :param screen: The data to be sent.
        """
        client.send(pickle.dumps(screen))

    def recv_data_in_chunks(self, sock):
        """
        The function receives data from the client and loads it in chunks.
        :param sock: The client's socket.
        :return: The function returns the received data.
        :rtype: list.
        """
        BUFF_SIZE = 4096  # 4 KiB
        data = b''
        while True:
            part = sock.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                # either 0 or end of data
                break
        return pickle.loads(data)

    def disconnect_client(self, client):
        client.send(pickle.dumps(["goodbye"]))
        self.clients_lst.remove(client)

        # try:
        #     return pickle.loads(data)
        # except EOFError:
        #     print("APP CLOSED")
