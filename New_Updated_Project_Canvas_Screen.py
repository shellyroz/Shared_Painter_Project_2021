import tkinter as tk
from tkinter import colorchooser
from functools import partial
import tkinter.messagebox

from PIL import ImageTk, Image

import pyautogui

from sign_up_database1 import Users
from login_database1 import Users1
from Project_Email_Handle import EmailBot
from Project_Server_Canvas_Trial import Server1


class CanvasScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.server = Server1('192.168.1.35', 1730)
        # self.server = Server('172.19.225.89', 1730)
        self.initial_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.about_us_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.sign_up_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.login_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.login_code_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.forgot_password_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.change_password_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.change_password_new_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100,
                                                  width=2000)
        self.canvas_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), width=460, height=720)
        self.logo_photo = ImageTk.PhotoImage(Image.open('small_project_logo_png.png'))
        self.logo_label = tk.Label(self.canvas_frame, image=self.logo_photo)
        self.root.title("SHARED PAINTER - CANVAS")
        # self.is_login_pressed = False
        # self.is_sign_up_pressed = False
        self.cursor = 'spider'
        # self.canvas_frame = tk.Frame(self.root)
        self.photo = tk.PhotoImage(width=1500, height=1100)  # w=900
        self.canvas_label = tk.Label(self.root, image=self.photo, cursor=self.cursor)
        self.color = "#000000"
        self.brush_sizes_lst = []
        self.brush_size = 1
        self.brush_types_lst = []
        self.brush_type = "●"
        self.mouse_x_positions_lst = []
        self.stop_drawing = False
        self.positions_lst = []
        self.running = True
        # self.sign_up_database = Users()
        # self.login_database = Users1()
        # self.email_sender = EmailBot()
        self.code_incorrect_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151))
        self.current_username = ''

    def create_screen(self):
        # x = self.root.winfo_screenwidth()
        # y = self.root.winfo_screenwidth()
        # x = 1800
        # y = 1100
        x = 2000
        y = 1100
        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 0, 151)
        self.root["background"] = bg_color

    # def database_stuff(self):
    #     global entry1
    #     global entry2
    #     global entry3
    #
    #     entry1 = email_str.get()
    #     entry2 = username_str.get()
    #     entry3 = password_str.get()

    # users_object = Users()
    # users_object.insert_user(email_str, username_str, password_str)

    def back_to_sign_up(self):
        '''
        The function returns to the sign up screen after going back to the home screen from the sign up screen.
        '''
        self.initial_frame.pack_forget()
        self.sign_up_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.sign_up_frame.pack(pady=205)

        bg_color = "#%02x%02x%02x" % (243, 249, 151)

        sign_up_font = ("Segoe Print", 15)

        email_label = tk.Label(self.sign_up_frame, text="Email: ", bg=bg_color, font=sign_up_font)
        email_label.pack()
        email_entry = tk.Entry(self.sign_up_frame, font=sign_up_font)
        email_entry.pack(pady=10)

        username_label = tk.Label(self.sign_up_frame, text="Username: ", bg=bg_color, font=sign_up_font)
        username_label.pack()
        username_entry = tk.Entry(self.sign_up_frame, font=sign_up_font)
        username_entry.pack(pady=10)

        password_label = tk.Label(self.sign_up_frame, text="Password: ", bg=bg_color, font=sign_up_font)
        password_label.pack()
        password_entry = tk.Entry(self.sign_up_frame, show="*", font=sign_up_font)
        password_entry.pack(pady=10)

        # B = tk.Button(self.sign_up_frame, text="OK - SIGN UP", command=database_stuff)
        B = tk.Button(self.sign_up_frame, text="OK - SIGN UP", bg="DarkBlue", font=sign_up_font,
                      fg='snow',
                      command=lambda: self.sign_up_database_stuff(email_entry, username_entry, password_entry))
        B.pack(side='left', padx=20, pady=20)

        back_home = tk.Button(self.sign_up_frame, text="BACK", bg="DarkBlue", font=sign_up_font,
                              fg='snow', command=self.back_from_sign_up)
        back_home.pack(side='right', padx=20, pady=20)

        self.root.title(f"SHARED PAINTER - SIGN UP")

        # print(self.is_sign_up_pressed)

        self.root.mainloop()

    def back_from_sign_up(self):
        '''
        The function returns to the home screen from the sign up screen.
        '''
        self.sign_up_frame.pack_forget()
        # self.initial_frame.pack_forget()
        self.back_to_initial_screen()

    def sign_up_database_stuff(self, email_entry, username_entry, password_entry):
        '''
        The function sends a new client's sign up information to the server,
        which logs it into the designated sign up database.
        :param email_entry: The new client's email entry.
        :param username_entry: The new client's username entry.
        :param password_entry: The new client's password entry.
        '''
        # global entry1
        # global entry2
        # global entry3

        entry1 = email_entry.get()
        entry2 = username_entry.get()
        entry3 = password_entry.get()

        print(entry1)
        print(entry2)
        print(entry3)

        self.server.sign_up(entry1, entry2, entry3)

        # users_object = Users()
        # users_object.insert_user(entry1, entry2, entry3)

        # self.sign_up_database.insert_user(entry1, entry2, entry3)
        # self.sign_up_database.create_users_list()

        # self.sign_up_database.print_users()
        # print(self.sign_up_database.users_list)

        # self.sign_ups_list.append(self.sign_up_database.users_list)

        self.root.title(f"SHARED PAINTER - {entry2}")

        self.sign_up_frame.pack_forget()
        self.design_canvas_screen()
        self.run()

    def design_sign_up_screen(self):
        '''
        The function creates the main screen used during sign ups.
        '''
        self.initial_frame.pack_forget()

        # x = self.root.winfo_screenwidth()
        # y = self.root.winfo_screenwidth()

        # x = 1800
        # y = 1100

        x = 2000
        y = 1100

        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        self.sign_up_frame.pack(pady=205)
        # canvas = tk.Canvas(self.root, width=441, height=200)
        # canvas.pack()
        # img = tk.PhotoImage(file="project_logo_png.png")
        # canvas.create_image(222, 102, image=img)

        # button = tk.Button(text="PRESS ME", command=self.database_stuff(email_str, username_str, password_str))
        # button.pack()
        # users_object = Users()
        # users_object.insert_user(email_str, username_str, password_str)

        # def database_stuff():
        #     self.is_sign_up_pressed = True
        #     global entry1
        #     global entry2
        #     global entry3
        #
        #     entry1 = email_entry.get()
        #     entry2 = username_entry.get()
        #     entry3 = password_entry.get()
        #
        #     print(entry1)
        #     print(entry2)
        #     print(entry3)
        #
        #     # users_object = Users()
        #     # users_object.insert_user(entry1, entry2, entry3)
        #     self.sign_up_database.insert_user(entry1, entry2, entry3)
        #     self.sign_up_database.create_users_list()
        #
        #     if self.is_sign_up_pressed:
        #         self.sign_up_frame.pack_forget()
        #         self.design_canvas_screen()
        #         self.run()

        # self.login_frame.destroy()
        # self.login_frame.pack_forget()
        # frame2 = tk.Frame(self.root)
        # frame2.pack()

        # self.root = tk.Tk()

        # email_label = tk.Label(self.root, text="Email: ")
        # email_label.pack()
        # email_entry = tk.Entry(self.root)
        # email_entry.pack(pady=10)
        #
        # username_label = tk.Label(self.root, text="Username: ")
        # username_label.pack()
        # username_entry = tk.Entry(self.root)
        # username_entry.pack(pady=10)
        #
        # password_label = tk.Label(self.root, text="Password: ")
        # password_label.pack()
        # password_entry = tk.Entry(self.root)
        # password_entry.pack(pady=10)

        sign_up_font = ("Segoe Print", 15)

        email_label = tk.Label(self.sign_up_frame, text="Email: ", bg=bg_color, font=sign_up_font)
        email_label.pack()
        email_entry = tk.Entry(self.sign_up_frame, font=sign_up_font)
        email_entry.pack(pady=10)

        username_label = tk.Label(self.sign_up_frame, text="Username: ", bg=bg_color, font=sign_up_font)
        username_label.pack()
        username_entry = tk.Entry(self.sign_up_frame, font=sign_up_font)
        username_entry.pack(pady=10)

        password_label = tk.Label(self.sign_up_frame, text="Password: ", bg=bg_color, font=sign_up_font)
        password_label.pack()
        password_entry = tk.Entry(self.sign_up_frame, show="*", font=sign_up_font)
        password_entry.pack(pady=10)

        # B = tk.Button(self.sign_up_frame, text="OK - SIGN UP", command=database_stuff)
        B = tk.Button(self.sign_up_frame, text="OK - SIGN UP", bg="DarkBlue", font=sign_up_font,
                      fg='snow',
                      command=lambda: self.sign_up_database_stuff(email_entry, username_entry, password_entry))
        B.pack(side='left', padx=20, pady=20)

        back_home = tk.Button(self.sign_up_frame, text="BACK", bg="DarkBlue", font=sign_up_font,
                              fg='snow', command=self.back_from_sign_up)
        back_home.pack(side='right', padx=20, pady=20)

        # print(self.is_sign_up_pressed)

        self.root.title(f"SHARED PAINTER - SIGN UP")

        self.root.mainloop()

        # print(self.is_sign_up_pressed)

    def back_to_login(self):
        '''
        The function returns to the login screen after going back to the home screen from the login screen.
        '''
        self.initial_frame.pack_forget()
        self.login_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.login_frame.pack(pady=250)

        bg_color = "#%02x%02x%02x" % (243, 249, 151)

        login_font = ("Segoe Print", 15)

        username_label = tk.Label(self.login_frame, text="Username: ", bg=bg_color, font=login_font)
        username_label.pack()
        username_entry = tk.Entry(self.login_frame, font=login_font)
        username_entry.pack(pady=10)

        password_label = tk.Label(self.login_frame, text="Password: ", bg=bg_color, font=login_font)
        password_label.pack()
        password_entry = tk.Entry(self.login_frame, show="*", font=login_font)
        password_entry.pack(pady=10)

        # B = tk.Button(self.login_frame, text="OK - LOGIN", command=database_stuff)
        B = tk.Button(self.login_frame, text="OK - LOGIN", bg="DarkBlue", font=login_font, fg='snow',
                      command=lambda: self.login_database_stuff(username_entry, password_entry))
        B.pack(side='left', padx=20, pady=20)

        back_home = tk.Button(self.login_frame, text="BACK", bg="DarkBlue", font=login_font,
                              fg='snow', command=self.back_from_login)
        back_home.pack(padx=20, pady=20, anchor='center')

        forgot_password_button = tk.Button(self.login_frame, text="Forgot" + "\n" + "Password", bg="DarkBlue",
                                           font=login_font,
                                           fg='snow', command=self.forgot_password_screen)
        forgot_password_button.pack(side='right', padx=20, pady=20)

        # go_back_button = tk.Button(self.login_frame, text="BACK", command=self.design_initial_screen)
        # go_back_button.pack()
        self.root.title(f"SHARED PAINTER - LOGIN")

        self.root.mainloop()

    def back_from_login(self):
        '''
        The function returns to the home screen from the login screen.
        '''
        self.login_frame.pack_forget()
        self.back_to_initial_screen()

    def login_database_stuff(self, username_entry, password_entry):
        '''
        The function sends a client's login information to the server,
        which logs it into the designated login database.
        :param username_entry: The client's username entry.
        :param password_entry: The client's password entry.
        '''
        # self.is_login_pressed = True
        # global entry2
        # global entry3

        entry2 = username_entry.get()
        entry3 = password_entry.get()

        print(entry2)
        print(entry3)

        # users1_object = Users1()
        # users1_object.insert_user(entry1, entry2, entry3)
        # users1_object.insert_user(entry2, entry3)
        # users1_object.create_users_list()

        # self.login_database.insert_user(entry2, entry3)
        # self.login_database.create_users_list()

        # self.sign_up_database.print_users()
        # self.login_database.print_users()

        # self.sign_up_database.create_users_list()
        # print(self.sign_up_database.users_list)
        # print(self.login_database.users_list)

        ''' IMPORTANT: self.root.title(f"SHARED PAINTER - {entry2}") '''
        self.current_username = entry2

        # self.server.login(entry2, entry3)

        can_continue = self.server.login(entry2, entry3)

        if can_continue == "ok":
            self.login_code_screen()

        else:
            self.login_frame.pack_forget()
            self.back_to_login()

        # rtrn = self.sign_up_database.is_user_in_database(entry2, entry3)
        #
        # print(rtrn)
        #
        # if "ERROR" not in rtrn:
        #     # self.login_frame.pack_forget()
        #     users_email = rtrn
        #     self.email_sender.send_email(users_email)
        #     self.login_code_screen(self.email_sender.code)
        #     print("given code is: " + self.email_sender.code)
        #
        # elif rtrn == "U_ERROR" or rtrn == "P_ERROR":
        #     self.login_frame.pack_forget()
        #     self.back_to_login()
        #     print(rtrn)

    def is_entered_code_ok(self, code_entry):
        '''
        The function sends the client's entered code to the server, which checks whether the
        code is correct or not. If the code is correct, the canvas screen is displayed and
        the client's login process is complete. If the code is incorrect, the client is requested
        to re-enter it.
        :param code_entry: The client's code entry.
        '''
        self.login_code_frame.pack_forget()
        self.code_incorrect_frame.pack_forget()

        # entered_code = code_entry.get()
        # print("entered code is: " + entered_code)

        login_code_font = ("Segoe Print", 20)
        bg_color = "#%02x%02x%02x" % (243, 249, 151)

        is_code_ok = self.server.is_login_code_ok(code_entry)

        if is_code_ok:
            self.design_canvas_screen()
            self.run()

        else:
            self.code_incorrect_frame.pack(pady=400)

            code_incorrect_label = tk.Label(self.code_incorrect_frame,
                                            text="The code you entered is incorrect. Please try again: ", bg=bg_color,
                                            font=login_code_font)
            code_incorrect_label.pack()

            code_entry = tk.Entry(self.code_incorrect_frame, font=login_code_font)
            code_entry.pack(pady=10)

            check_code_button = tk.Button(self.code_incorrect_frame, text='Continue', bg="DarkBlue",
                                          font=login_code_font,
                                          fg='snow', command=lambda: self.is_entered_code_ok(code_entry))
            check_code_button.pack()

            # self.root.mainloop()

    def login_code_screen(self):
        '''
        The function creates the screen displayed to clients during logins, where
        they are requested to enter the code sent to their email address.
        '''
        self.login_frame.pack_forget()
        self.login_code_frame.pack(pady=400)

        login_code_font = ("Segoe Print", 20)
        bg_color = "#%02x%02x%02x" % (243, 249, 151)

        code_label = tk.Label(self.login_code_frame, text="Please enter the code you received via email:  ",
                              bg=bg_color, font=login_code_font)
        code_label.pack()
        code_entry = tk.Entry(self.login_code_frame, font=login_code_font)
        code_entry.pack(pady=10)

        check_code_button = tk.Button(self.login_code_frame, text='Continue', bg="DarkBlue", font=login_code_font,
                                      fg='snow', command=lambda: self.is_entered_code_ok(code_entry))
        check_code_button.pack()

        self.root.title(f"SHARED PAINTER - LOGIN")

    '''FORGOT PASSWORD'''

    def continue_after_changing_password(self):
        '''
        The function returns to the login screen after changing a client's password.
        '''
        self.change_password_frame.pack_forget()
        self.back_to_login()

    def change_password(self, entered_username, password_entry):
        '''
        The function sends a client's entered username and new password to the server, which
        updates the designated database.
        :param entered_username: The client's entered username.
        :param password_entry: The client's entered new password.
        '''
        new_password = password_entry.get()

        # self.change_password_frame.pack(pady=400)
        #
        # B.pack_forget()

        bg_color = "#%02x%02x%02x" % (243, 249, 151)

        login_font = ("Segoe Print", 15)

        print("This is the new password:")
        print(new_password)
        # self.sign_up_database.change_password(entered_username, new_password)
        self.server.change_to_new_password(entered_username, new_password)

        self.continue_after_changing_password()

        # password_label = tk.Label(self.change_password_new_frame, text="Please enter your new password: ", bg=bg_color,
        #                           font=login_font)
        # password_label.pack()
        # password_entry = tk.Entry(self.change_password_new_frame, font=login_font)
        # password_entry.pack(pady=10)

        # continue_button = tk.Button(self.change_password_frame, text='go', font=login_font,
        #                             command=self.continue_after_changing_password)
        # continue_button.pack()

    def change_password_screen(self, entered_username):
        '''
        The function creates the second screen displayed to clients when they click "forgot password",
        which they see if the username they entered is in the designated database. In this screen,
        the clients are requested to enter a new password.
        :param entered_username: The client's entered username.
        '''
        self.forgot_password_frame.pack_forget()
        self.change_password_frame.pack(pady=400)

        bg_color = "#%02x%02x%02x" % (243, 249, 151)

        login_font = ("Segoe Print", 15)

        password_label = tk.Label(self.change_password_frame, text="Please enter your new password: ", bg=bg_color,
                                  font=login_font)
        password_label.pack()
        password_entry = tk.Entry(self.change_password_frame, show="*", font=login_font)
        password_entry.pack(pady=10)

        print("PASSWORD ENTRY GET: " + password_entry.get())

        # new_password = password_entry.get()
        # self.change_password(entered_username, password_entry)
        B = tk.Button(self.change_password_frame, text='Continue', bg="DarkBlue", font=login_font, fg='snow',
                      command=lambda: self.change_password(entered_username, password_entry, B))
        B.pack()

        self.root.title(f"SHARED PAINTER - FORGOT PASSWORD")

    def check_and_change_password(self, username_entry):
        '''
        The function sends the username a client entered to the server, which checks whether it's
        in the designated database or not. If the username is in the database, the client's password can be changed.
        If not, an error message is displayed and the client is requested to re-enter the username.
        :param username_entry: The client's username entry.
        '''
        # self.sign_up_database.create_users_list()
        entered_username = username_entry.get()
        print(entered_username)
        # can_change_password = self.sign_up_database.is_username_in_database(entered_username)
        # # print(self.sign_up_database.users_list)
        # print(can_change_password)

        can_change_password = self.server.check_to_change_password(entered_username)

        if can_change_password:
            self.change_password_screen(entered_username)

        else:
            tk.messagebox.showerror(title="ERROR",
                                    message="The username you entered is incorrect. Please try again.")
            self.forgot_password_frame.pack_forget()
            self.back_to_forgot_password_screen()

    def back_to_forgot_password_screen(self):
        '''
        The function returns to the "forgot password" screen after going back to the login
        screen from the "forgot password" screen.
        '''
        self.login_frame.pack_forget()
        self.forgot_password_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)

        bg_color = "#%02x%02x%02x" % (243, 249, 151)

        login_font = ("Segoe Print", 15)

        username_label = tk.Label(self.forgot_password_frame, text="Please enter your username: ", bg=bg_color,
                                  font=login_font)
        username_label.pack()
        username_entry = tk.Entry(self.forgot_password_frame, font=login_font)
        username_entry.pack(pady=10)

        check_username_button = tk.Button(self.forgot_password_frame, text='Continue', bg="DarkBlue", font=login_font,
                                          fg='snow', command=lambda: self.check_and_change_password(username_entry))
        check_username_button.pack()

        self.root.title(f"SHARED PAINTER - FORGOT PASSWORD")

    def forgot_password_screen(self):
        '''
        The function creates the first screen displayed to clients when they click "forgot password",
        where they enter their username.
        '''
        self.login_frame.pack_forget()
        self.forgot_password_frame.pack(pady=400)

        bg_color = "#%02x%02x%02x" % (243, 249, 151)

        login_font = ("Segoe Print", 15)

        username_label = tk.Label(self.forgot_password_frame, text="Please enter your username: ", bg=bg_color,
                                  font=login_font)
        username_label.pack()
        username_entry = tk.Entry(self.forgot_password_frame, font=login_font)
        username_entry.pack(pady=10)

        check_username_button = tk.Button(self.forgot_password_frame, text='Continue', bg="DarkBlue", font=login_font,
                                          fg='snow', command=lambda: self.check_and_change_password(username_entry))
        check_username_button.pack()

        self.root.title(f"SHARED PAINTER - FORGOT PASSWORD")

    '''FORGOT PASSWORD'''

    def design_login_screen(self):
        '''
        The function creates the main screen used during logins.
        '''
        self.initial_frame.pack_forget()

        # x = self.root.winfo_screenwidth()
        # y = self.root.winfo_screenwidth()
        # x = 1800
        # y = 1100

        x = 2000
        y = 1100

        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        self.root.title(f"SHARED PAINTER - LOGIN")

        self.login_frame.pack(pady=250)
        # canvas = tk.Canvas(self.root, width=441, height=200)
        # canvas.pack()
        # img = tk.PhotoImage(file="project_logo_png.png")
        # canvas.create_image(222, 102, image=img)

        # button = tk.Button(text="PRESS ME", command=self.database_stuff(email_str, username_str, password_str))
        # button.pack()
        # users_object = Users()
        # users_object.insert_user(email_str, username_str, password_str)

        # def database_stuff():
        #     self.is_login_pressed = True
        #     # global entry1
        #     global entry2
        #     global entry3
        #
        #     # entry1 = email_entry.get()
        #     entry2 = username_entry.get()
        #     entry3 = password_entry.get()
        #
        #     # print(entry1)
        #     print(entry2)
        #     print(entry3)
        #
        #     # users1_object = Users1()
        #     # users1_object.insert_user(entry1, entry2, entry3)
        #     # users1_object.insert_user(entry2, entry3)
        #     # users1_object.create_users_list()
        #     self.login_database.insert_user(entry2, entry3)
        #     self.login_database.create_users_list()
        #
        #     self.logins_list = self.login_database.users_list
        #
        #
        #     if self.is_login_pressed:
        #         # email_label.pack_forget()
        #         # email_entry.pack_forget()
        #         # username_label.pack_forget()
        #         # username_entry.pack_forget()
        #         # password_label.pack_forget()
        #         # password_entry.pack_forget()
        #         # B.pack_forget()
        #         self.root.title(f"SHARED PAINTER - {entry2}")
        #
        #         # print(self.sign_up_database.users_list)
        #         # print(self.login_database.users_list)
        #
        #         print(self.sign_ups_list)
        #         print(self.logins_list)
        #
        #         # print(self.sign_up_database.is_user_in_database(entry2, entry3))
        #         if self.sign_up_database.is_user_in_database(entry2, entry3) != "ERROR":
        #             self.login_frame.pack_forget()
        #             users_email = self.sign_up_database.is_user_in_database(entry2, entry3)
        #             self.email_sender.send_email(users_email)
        # self.design_canvas_screen()
        # self.run_canvas()

        # self.login_frame.destroy()
        # self.login_frame.pack_forget()
        # frame2 = tk.Frame(self.root)
        # frame2.pack()

        # self.root = tk.Tk()

        # email_label = tk.Label(self.root, text="Email: ")
        # email_label.pack()
        # email_entry = tk.Entry(self.root)
        # email_entry.pack(pady=10)
        #
        # username_label = tk.Label(self.root, text="Username: ")
        # username_label.pack()
        # username_entry = tk.Entry(self.root)
        # username_entry.pack(pady=10)
        #
        # password_label = tk.Label(self.root, text="Password: ")
        # password_label.pack()
        # password_entry = tk.Entry(self.root)
        # password_entry.pack(pady=10)

        # email_label = tk.Label(self.login_frame, text="Email: ")
        # email_label.pack()
        # email_entry = tk.Entry(self.login_frame)
        # email_entry.pack(pady=10)

        login_font = ("Segoe Print", 15)

        username_label = tk.Label(self.login_frame, text="Username: ", bg=bg_color, font=login_font)
        username_label.pack()
        username_entry = tk.Entry(self.login_frame, font=login_font)
        username_entry.pack(pady=10)

        password_label = tk.Label(self.login_frame, text="Password: ", bg=bg_color, font=login_font)
        password_label.pack()
        password_entry = tk.Entry(self.login_frame, show="*", font=login_font)
        password_entry.pack(pady=10)

        # B = tk.Button(self.login_frame, text="OK - LOGIN", command=database_stuff)
        B = tk.Button(self.login_frame, text="OK - LOGIN", bg="DarkBlue", font=login_font, fg='snow',
                      command=lambda: self.login_database_stuff(username_entry, password_entry))
        B.pack(side='left', padx=20, pady=20)

        back_home = tk.Button(self.login_frame, text="BACK", bg="DarkBlue",
                              font=login_font, fg='snow', command=self.back_from_login)
        back_home.pack(padx=20, pady=20, anchor='center')

        forgot_password_button = tk.Button(self.login_frame, text="Forgot" + "\n" + "Password", bg="DarkBlue",
                                           font=login_font, fg='snow', command=self.forgot_password_screen)
        forgot_password_button.pack(side='right', padx=20, pady=20)

        # go_back_button = tk.Button(self.login_frame, text="BACK", command=self.design_initial_screen)
        # go_back_button.pack()

        self.root.mainloop()

        # self.root.mainloop()

    def back_from_about_us(self):
        '''
        The function returns to the home screen from the "about us" screen.
        '''
        self.about_us_frame.pack_forget()
        self.back_to_initial_screen()

    def back_to_about_us(self):
        '''
        The function returns to the "about us" screen after going back to the home screen from the "about us" screen.
        '''
        self.initial_frame.pack_forget()

        self.about_us_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.about_us_frame.pack()

        x = 2000
        y = 1100

        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        self.root.title(f"SHARED PAINTER - ABOUT US")

        self.about_us_frame.pack(pady=20)

        about_us_text = '''Shared Painter has a simple purpose: building connections between people.
        This goal is obtained by using art to encourage collaboration between individuals, showing
        that despite our differences, together we can create great things.

        Simply choose a color, a brush size, and draw away! You will be sharing a canvas with other
        users and painting on it simultaneously, eventually producing a one-of-a-kind masterpiece.'''

        about_us_label = tk.Label(self.about_us_frame, text=about_us_text, bg=bg_color, font=("Segoe Print", 15))
        about_us_label.pack(pady=150, anchor='center')

        back_home = tk.Button(self.about_us_frame, text="BACK", bg="DarkBlue", font=("Segoe Print", 16),
                              fg='snow', command=self.back_from_about_us)
        back_home.pack()

        self.root.mainloop()

    def design_about_us_screen(self):
        '''
        The function creates the information screen displayed when the "about us"
        button is pressed.
        '''
        self.initial_frame.pack_forget()

        x = 2000
        y = 1100

        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        self.root.title(f"SHARED PAINTER - ABOUT US")

        self.about_us_frame.pack(pady=20)

        about_us_text = '''Shared Painter has a simple purpose: building connections between people.
        This goal is obtained by using art to encourage collaboration between individuals, showing
        that despite our differences, together we can create great things.

        Simply choose a color, a brush size, and draw away! You will be sharing a canvas with other
        users and painting on it simultaneously, eventually producing a one-of-a-kind masterpiece.'''

        about_us_label = tk.Label(self.about_us_frame, text=about_us_text, bg=bg_color, font=("Segoe Print", 15))
        about_us_label.pack(pady=150, anchor='center')

        back_home = tk.Button(self.about_us_frame, text="BACK", bg="DarkBlue", font=("Segoe Print", 16),
                              fg='snow', command=self.back_from_about_us)
        back_home.pack()

        self.root.mainloop()

    def design_initial_screen(self):
        '''
        The function creates the app's home screen.
        '''
        # x = self.root.winfo_screenwidth()
        # y = self.root.winfo_screenwidth()

        # x = 1800
        # y = 1100

        x = 2000
        y = 1100

        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        self.initial_frame.pack()

        logo_photo = ImageTk.PhotoImage(Image.open('project_logo_png.png'))
        logo_label = tk.Label(self.initial_frame, image=logo_photo)
        logo_label.pack(pady=95)

        login_button = tk.Button(self.initial_frame, text="LOGIN", bg="DarkBlue", font=("Segoe Print", 14),
                                 fg="snow", height=2, width=12, command=self.design_login_screen)
        # login_button.pack(padx=400, pady=150)
        login_button.pack(padx=60, pady=100, side='left')

        '''padx=150, pady=430, side=tk.LEFT'''

        sign_up_button = tk.Button(self.initial_frame, text="SIGN UP", bg="DarkBlue", font=("Segoe Print", 14),
                                   fg="snow", height=2, width=12, command=self.design_sign_up_screen)
        # sign_up_button.pack(padx=700, pady=250)
        sign_up_button.pack(padx=60, pady=100, side='right')

        about_us_button = tk.Button(self.initial_frame, text="ABOUT US", bg="DarkBlue", font=("Segoe Print", 14),
                                    fg="snow", height=2, width=12, command=self.design_about_us_screen)
        # sign_up_button.pack(padx=700, pady=250)
        about_us_button.pack(padx=60, pady=100, anchor='center')

        # color_palate_button = tk.Button(frame, text="Color Palette", bg="medium violet red", fg="snow",
        #                                height=2, width=10, command=choose_color)

        self.root.title(f"SHARED PAINTER - HOME")

        self.root.mainloop()

    def back_to_initial_screen(self):
        '''
        The function returns to the app's home screen after displaying a different screen.
        '''
        self.initial_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)

        self.initial_frame.pack()

        logo_photo = ImageTk.PhotoImage(Image.open('project_logo_png.png'))
        logo_label = tk.Label(self.initial_frame, image=logo_photo)
        logo_label.pack(pady=70)

        login_button = tk.Button(self.initial_frame, text="LOGIN", bg="DarkBlue", font=("Segoe Print", 14),
                                 fg="snow", height=2, width=12, command=self.back_to_login)
        # login_button.pack(padx=400, pady=150)
        login_button.pack(padx=60, pady=100, side='left')

        '''padx=150, pady=430, side=tk.LEFT'''

        sign_up_button = tk.Button(self.initial_frame, text="SIGN UP", bg="DarkBlue", font=("Segoe Print", 14),
                                   fg="snow", height=2, width=12, command=self.back_to_sign_up)
        # sign_up_button.pack(padx=700, pady=250)
        sign_up_button.pack(padx=60, pady=100, side='right')

        about_us_button = tk.Button(self.initial_frame, text="ABOUT US", bg="DarkBlue", font=("Segoe Print", 14),
                                    fg="snow", height=2, width=12, command=self.back_to_about_us)
        # sign_up_button.pack(padx=700, pady=250)
        about_us_button.pack(padx=60, pady=100, anchor='center')

        self.root.title(f"SHARED PAINTER - HOME")

        self.root.mainloop()

    def chosen_size(self, sizes_Lb):
        '''
        The function sets the client's chosen brush size as the current brush size.
        :param sizes_Lb: The brush size listbox created.
        '''
        chosen_value = sizes_Lb.curselection()[0] + 1
        self.brush_sizes_lst.append(chosen_value)

        if self.brush_sizes_lst != []:
            self.brush_size = self.brush_sizes_lst[-1]

    def choose_brush_size(self):
        '''
        The function creates the brush sizes listbox, displaying the brush sizes the client
        can choose from to draw on the canvas.
        '''
        screen = tk.Tk()
        screen.title("Brush Size")

        sizes_Lb = tk.Listbox(screen)
        sizes_Lb.bind('<<ListboxSelect>>', lambda x: self.chosen_size(sizes_Lb))
        sizes_Lb.pack()

        for i in range(1, 11):
            sizes_Lb.insert(i, i)

        # sizes_Lb.insert(1, 1)
        # sizes_Lb.insert(2, 2)
        # sizes_Lb.insert(3, 3)
        # sizes_Lb.insert(4, 4)

        screen.mainloop()

    def chosen_type(self, types_Lb):
        '''
        The function sets the client's chosen brush type as the current brush type.
        :param types_Lb: The brush type listbox created.
        '''
        chosen_value_index = types_Lb.curselection()[0]
        if chosen_value_index == 0:
            chosen_value = '●'

        elif chosen_value_index == 1:
            chosen_value = '*'

        self.brush_types_lst.append(chosen_value)
        print(chosen_value)

        if self.brush_types_lst != []:
            self.brush_type = self.brush_types_lst[-1]

    def choose_brush_type(self):
        '''
        The function creates the brush type listbox, displaying the brush types the client
        can choose from to draw on the canvas.
        '''
        screen = tk.Tk()
        screen.title("Brush Type")

        types_Lb = tk.Listbox(screen)
        types_Lb.bind('<<ListboxSelect>>', lambda x: self.chosen_type(types_Lb))
        types_Lb.pack()

        types_Lb.insert(1, "●")
        types_Lb.insert(2, "*")

        screen.mainloop()

    def choose_color(self):
        '''
        The function creates the color palette widget, displaying the colors and shades the
        client can choose from to draw on the canvas.
        '''
        # variable to store hexadecimal code of color
        color_code = colorchooser.askcolor(title="Color Palette")
        print("Shelly Rozman")
        self.color = color_code[1]
        print("dA GAMBIT")
        print(color_code)

    def design_canvas_screen(self):
        '''
        The function creates the app's canvas screen.
        '''
        # x = self.root.winfo_screenwidth()
        # y = self.root.winfo_screenwidth()
        # x = 1800
        # y = 1100

        x = 2000
        y = 1100

        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        self.canvas_frame.pack(side=tk.LEFT)
        self.logo_label.photo = self.logo_photo
        self.logo_label.pack(side='top', pady=70)

        '''def choose_color():
            # variable to store hexadecimal code of color
            color_code = colorchooser.askcolor(title="Color Palette")
            print("Shelly Rozman")
            self.color = color_code[1]
            print("dA GAMBIT")
            print(color_code)'''

        bg_color = "#%02x%02x%02x" % (243, 249, 151)

        # canvas_frame = tk.Frame(self.root, width=460, height=720, bg=bg_color)
        # self.canvas_frame.pack(side=tk.LEFT)

        # logo_photo = ImageTk.PhotoImage(Image.open('small_project_logo_png.png'))
        # logo_label = tk.Label(self.canvas_frame, image=logo_photo)
        # logo_label.pack()

        # color_palate_button = tk.Button(frame, text="Color Palette", bg="medium violet red", fg="snow",
        #                                 height=2, width=10, command=choose_color)
        color_palate_button = tk.Button(self.canvas_frame, text="Color Palette", bg="medium violet red",
                                        font=("Segoe Print", 11),
                                        fg="snow", height=2, width=10, command=self.choose_color)
        # # color_palate_button.place(x=10, y=10)
        # color_palate_button.pack(side=tk.LEFT, padx=10, pady=10)
        color_palate_button.pack(padx=120, pady=10)
        #
        eraser_button = tk.Button(self.canvas_frame, text="Eraser", bg="medium violet red", font=("Segoe Print", 11),
                                  fg="snow", height=2, width=10, command=self.set_color_as_eraser)
        # eraser_button.pack(side=tk.RIGHT, padx=10, pady=10)
        eraser_button.pack(padx=120, pady=10)

        brush_type_button = tk.Button(self.canvas_frame, text="Brush Type", bg="medium violet red",
                                      font=("Segoe Print", 11),
                                      fg="snow", height=2, width=10, command=self.choose_brush_type)
        # brush_type_button.pack(side=tk.BOTTOM, pady=10, anchor='center')
        brush_type_button.pack(padx=120, pady=10)
        # color_palate_button.lower()
        #
        brush_size_button = tk.Button(self.canvas_frame, text="Brush Size", bg="medium violet red",
                                      font=("Segoe Print", 11),
                                      fg="snow", height=2, width=10, command=self.choose_brush_size)
        # # brush_size_button.place(x=10, y=80)
        # brush_size_button.pack(padx=10, pady=10, anchor='center')
        brush_size_button.pack(padx=120, pady=10)
        # frame1 = tk.Frame(self.root, width=460, height=720, bg=bg_color)
        # frame1.pack(side=tk.LEFT)
        #
        # username_label = tk.Label(self, text="Username: ")
        # username_label.pack()
        # username_entry = tk.Entry(self)
        # username_entry.pack(pady=10)
        #
        # password_label = tk.Label(self, text="Password: ")
        # password_label.pack()
        # password_entry = tk.Entry(self)
        # password_entry.pack(pady=10)
        #
        # verify_password_label = tk.Label(self, text="Verify Password: ")
        # verify_password_label.pack()
        # verify_password_entry = tk.Entry(self)
        # verify_password_entry.pack(pady=10)

    # global photo
    # photo = tk.PhotoImage(width=900, height=650)
    #
    # def build_canvas(self):
    #     photo.place(x=150, y=50)

    # global stop_drawing
    # stop_drawing = False

    # def color_pixel(self, image, pos, color):
    #     """Place pixel at pos=(x,y) on image, with color=(r,g,b)."""
    #     if self.stop_drawing == False:
    #         r, g, b = color
    #         x, y = pos
    #         # image.put("#%02x%02x%02x" % (r, g, b), (x, y))
    #         image.put("#ffffff"%self.color, (x, y))
    #
    #     else:
    #         pass
    def color_pixel(self, pos):
        '''
        The function colors a single pixel in the given position on the canvas,
        in the current color used by the client.
        :param pos: The position of the pixel to be colored.
        '''
        """Place pixel at pos=(x,y) on image, with color=(r,g,b)."""
        if not self.stop_drawing:
            x, y = pos
            self.photo.put(self.color, (x, y))

        else:
            pass

    def set_color_as_eraser(self):
        '''
        The function sets the current used color to an eraser.
        '''
        self.color = '#f0f0f0'
        # self.cursor = 'circle'
        # self.canvas_label = tk.Label(self.root, image=self.photo, cursor=self.cursor)
        # self.canvas_label.pack()

    def color_pixel_for_server(self, pos, color):
        '''
        The function colors a single pixel in the given position on the canvas,
        in the given color.
        :param pos: The position of the pixel to be colored.
        :param color: The color of the pixel to be colored.
        '''
        """Place pixel at pos=(x,y) on image, with color=(r,g,b)."""
        self.photo.put(color, pos)

    def update_positions_lst(self, coords):
        '''
        The function updates the list of the colored pixels' positions on the canvas.
        :param coords: A pixel's position on the canvas.
        '''
        for coord in coords:
            if coord < 0:
                return
        self.positions_lst.append((self.color, coords, self.brush_size, self.brush_type))

    def detect_motion(self, event):
        '''
        The function detects the client's mouse motion on the canvas and sends
        the respective positions, according to the client's chosen brush size and type,
        to the "color_pixel" function.
        :param event:
        '''
        # x, y = event.x + 5, event.y + 25
        x, y = pyautogui.position()[0] - 415, pyautogui.position()[1]
        # real_x = pyautogui.position()[0]

        # if real_x < 326:
        # return
        # self.x_lst.append(x)
        # self.y_lst.append(y)
        # print(x)
        # current_color = self.color
        # if self.mouse_x_positions_lst != []:
        #     if (self.mouse_x_positions_lst[-1] - x) < -200:
        #         self.color = "#ffffff"

        # self.mouse_x_positions_lst.append(x)
        # print(self.mouse_x_positions_lst)

        # print(self.mouse_x_positions_lst[-2] - x)
        # color = (0, 0, 255)

        # self.color_pixel(self.photo, (x, y), self.color)
        # self.color_pixel(self.photo, (x + 1, y), self.color)
        # self.color_pixel(self.photo, (x, y + 1), self.color)
        # self.color_pixel(self.photo, (x + 1, y + 1), self.color)
        # self.color_pixel(self.photo, (x - 1, y), self.color)
        # self.color_pixel(self.photo, (x - 1, y + 1), self.color)
        # self.color_pixel(self.photo, (x - 1, y + 2), self.color)
        # self.color_pixel(self.photo, (x, y + 2), self.color)
        # self.color_pixel(self.photo, (x + 1, y + 2), self.color)

        # self.color_pixel((x, y))
        # self.positions_lst.append((self.color, (x, y)))
        # self.update_positions_lst((x, y))
        # self.positions_lst = [(self.color, (x, y))]

        # Color all pixels according to the brush size
        self.update_positions_lst((x, y))
        if self.brush_type == "●":
            for i in range(x, x + self.brush_size):
                for j in range(y, y + self.brush_size):
                    if x >= 0:
                        self.color_pixel((i, j))
                        # self.update_positions_lst((i, j))


        # TODO make something out of this - draws asterisks
        elif self.brush_type == "*":
            for i in range(self.brush_size):
                pixels_to_color = [(x, y), (x + i, y), (x + i, y + i), (x, y + i), (x - i, y), (x - i, y - i),
                                   (x, y - i)]
                # Eliminate repetitions
                pixels_to_color = list(set(pixels_to_color))
                # Color and append to the positions list every pixel in the list
                for pixel in pixels_to_color:
                    if x >= 0:
                        self.color_pixel(pixel)
                        # self.update_positions_lst(pixel)

        # Color all pixels according to the brush size
        # for i in range(self.brush_size):
        #     pixels_to_color = [(x + i, y), (x + i, y + i), (x, y + i)]
        #     # Eliminate repetitions
        #     pixels_to_color = list(set(pixels_to_color))
        #     # Color and append to the positions list every pixel in the list
        #     for pixel in pixels_to_color:
        #         self.color_pixel(pixel)
        #         self.update_positions_lst(pixel)

        'IMPORTANT'
        # for i in range(x, x + self.brush_size):
        #     for j in range(y, y + self.brush_size):
        #         self.color_pixel((i, j))
        #         self.update_positions_lst((i, j))

        """if self.brush_size == 2 or self.brush_size == 3 or self.brush_size == 4:
            self.color_pixel((x + 1, y))
            self.color_pixel((x, y + 1))
            self.color_pixel((x + 1, y + 1))
            self.update_positions_lst((x + 1, y))
            self.update_positions_lst((x, y + 1))
            self.update_positions_lst((x + 1, y + 1))
            # self.positions_lst.append((self.color, (x + 1, y)))
            # self.positions_lst.append((self.color, (x, y + 1)))
            # self.positions_lst.append((self.color, (x + 1, y + 1)))

        if self.brush_size == 3 or self.brush_size == 4:
            self.color_pixel((x - 1, y))
            self.color_pixel((x - 1, y + 1))
            self.color_pixel((x - 1, y + 2))
            self.color_pixel((x, y + 2))
            self.color_pixel((x + 1, y + 2))
            self.update_positions_lst((x - 1, y))
            self.update_positions_lst((x - 1, y + 1))
            self.update_positions_lst((x - 1, y + 2))
            self.update_positions_lst((x, y + 2))
            self.update_positions_lst((x + 1, y + 2))
            # self.positions_lst.append((self.color, (x - 1, y)))
            # self.positions_lst.append((self.color, (x - 1, y + 1)))
            # self.positions_lst.append((self.color, (x - 1, y + 2)))
            # self.positions_lst.append((self.color, (x, y + 2)))
            # self.positions_lst.append((self.color, (x + 1, y + 2)))


        if self.brush_size == 4:
            self.color_pixel((x + 2, y))
            self.color_pixel((x + 2, y + 1))
            self.color_pixel((x + 2, y + 2))
            self.color_pixel((x + 2, y + 3))
            self.color_pixel((x + 1, y + 3))
            self.color_pixel((x, y + 3))
            self.color_pixel((x - 1, y + 3))
            self.update_positions_lst((x + 2, y))
            self.update_positions_lst((x + 2, y + 1))
            self.update_positions_lst((x + 2, y + 2))
            self.update_positions_lst((x + 2, y + 3))
            self.update_positions_lst((x + 1, y + 3))
            self.update_positions_lst((x, y + 3))
            self.update_positions_lst((x - 1, y + 3))
            # self.positions_lst.append((self.color, (x + 2, y)))
            # self.positions_lst.append((self.color, (x + 2, y + 1)))
            # self.positions_lst.append((self.color, (x + 2, y + 2)))
            # self.positions_lst.append((self.color, (x + 2, y + 3)))
            # self.positions_lst.append((self.color, (x + 1, y + 3)))
            # self.positions_lst.append((self.color, (x, y + 3)))
            # self.positions_lst.append((self.color, (x - 1, y + 3)))





        # self.positions_lst.append(self.positions_lst)




        # self.color_pixel(self.photo, (x + 1, y))
        # self.color_pixel(self.photo, (x, y + 1))
        # self.color_pixel(self.photo, (x + 1, y + 1))
        # self.color_pixel(self.photo, (x - 1, y))
        # self.color_pixel(self.photo, (x - 1, y + 1))
        # self.color_pixel(self.photo, (x - 1, y + 2))
        # self.color_pixel(self.photo, (x, y + 2))
        # self.color_pixel(self.photo, (x + 1, y + 2))"""

    def pause_drawing(self, event):
        self.stop_drawing = True

    def resume_drawing(self, event):
        self.stop_drawing = False

    def setup(self):
        '''
        The fucntion displayes the app's home screen.
        '''
        self.root.protocol("WM_DELETE_WINDOW", self.on_quit)
        self.design_initial_screen()

    def on_quit(self):
        '''
        The function closes the app.
        '''
        self.running = False
        self.root.destroy()

    def run(self):
        '''
        The function calls the "run_canvas" function in order to display
        the app's canvas screen and detect motion.
        '''
        self.run_canvas()
        # self.gambit()
        self.root.mainloop()

    def run_canvas(self):
        '''
        The function binds the motion detector and creates the canvas clients draw on.
        '''
        self.root.bind('<B1-Motion>', self.detect_motion)
        # self.root.bind('<Button-1>', self.resume_drawing)
        # self.root.bind('<ButtonRelease-1>', self.stop_drawing)
        '''self.canvas_label = tk.Label(self.root, image=self.photo, cursor=self.cursor)'''
        # label = tk.Label(self.canvas_frame, image=self.photo)
        # label.grid()
        # label.place(x=100, y=0)
        self.canvas_label.pack()
        self.root.title(f"SHARED PAINTER - {self.current_username}")
        self.root.mainloop()


if __name__ == "__main__":
    app = CanvasScreen()
    # app.design_login_screen()
    app.design_initial_screen()
    # app.design_canvas_screen()
    # app.run_canvas()
    #
    # if app.is_login_pressed:
    #     print("Taylor Swift")
    # app.design_canvas_screen()
    # app.run_canvas()
    # app.design_canvas_screen()
    # app.run_canvas()
    # app.create_login_screen()