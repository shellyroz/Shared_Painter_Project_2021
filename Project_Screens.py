# Name: Shelly Rozman
# Python Version: 3.7.2
# Date: 14/3/2021
import pickle
import socket
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
import tkinter.messagebox
from PIL import ImageTk, Image
import pyautogui
import os
from Project_Server import Server


class Screens:
    def __init__(self, server_socket):
        self.root = tk.Tk()
        self.server = Server(socket.gethostbyname(socket.gethostname()), 1730)
        #self.server = Server('172.19.226.94', 1730)
        self.initial_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.about_us_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.sign_up_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.login_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.login_code_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.forgot_password_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.change_password_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
        self.change_password_new_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100,
                                                  width=2000)
        self.main_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100,
                                                  width=2000)
        self.my_canvas = tk.Canvas(self.main_frame, bg="#%02x%02x%02x" % (243, 249, 151))
        self.my_scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.my_canvas.yview)
        self.gallery_back_home = tk.Button(self.my_canvas, text="BACK", bg="DarkBlue", font=("Segoe Print", 16),
                              fg='snow', command=self.back_from_gallery_screen)
        self.canvas_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), width=460, height=720)
        self.logo_photo = ImageTk.PhotoImage(Image.open('small_project_logo_png.png'))
        self.logo_label = tk.Label(self.canvas_frame, image=self.logo_photo)
        self.root.title("SHARED PAINTER - CANVAS")
        self.cursor = 'pencil'
        self.photo = tk.PhotoImage(width=1500, height=1100) # w=900
        self.canvas_label = tk.Label(self.root, image=self.photo, cursor=self.cursor)
        self.color = "#000000"
        self.brush_sizes_lst = []
        self.brush_size = 1
        self.brush_types_lst = []
        self.brush_type = "●"
        #self.mouse_x_positions_lst = []
        self.running = True
        self.stop_drawing = False
        self.positions_lst = []
        #self.painted_pixels = []
        self.code_incorrect_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151))
        self.current_username = ''
        self.saved_screenshot_num = 1
        self.server_socket = server_socket


    def back_to_sign_up(self):
        """
        The function returns to the sign up screen after going back to the home screen from the sign up screen.
        """
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

        B = tk.Button(self.sign_up_frame, text="OK - SIGN UP", bg="DarkBlue", font=sign_up_font,
                      fg='snow',
                      command=lambda: self.sign_up_database_stuff(email_entry, username_entry, password_entry))
        B.pack(side='left', padx=20, pady=20)

        back_home = tk.Button(self.sign_up_frame, text="BACK", bg="DarkBlue", font=sign_up_font,
                              fg='snow', command=self.back_from_sign_up)
        back_home.pack(side='right', padx=20, pady=20)

        self.root.title(f"SHARED PAINTER - SIGN UP")

        self.root.mainloop()

    def back_from_sign_up(self):
        """
        The function returns to the home screen from the sign up screen.
        """
        self.sign_up_frame.pack_forget()
        self.back_to_initial_screen()

    def sign_up_database_stuff(self, email_entry, username_entry, password_entry):
        """
        The function sends a new client's sign up information to the server,
        which logs it into the designated sign up database.
        :param email_entry: The new client's email entry.
        :param username_entry: The new client's username entry.
        :param password_entry: The new client's password entry.
        """
        entered_email = email_entry.get()
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        print(entered_email)
        print(entered_username)
        print(entered_password)

        can_sign_up = self.server.sign_up(entered_email, entered_username, entered_password)

        if can_sign_up == "success":
            self.current_username = entered_username
            self.root.title(f"SHARED PAINTER - {self.current_username}")

            self.sign_up_frame.pack_forget()
            self.design_canvas_screen()
            self.run()

        elif can_sign_up == "error":
            self.sign_up_frame.pack_forget()
            self.back_to_sign_up()

    def design_sign_up_screen(self):
        """
        The function creates the main screen used during sign ups.
        """
        self.initial_frame.pack_forget()

        x = 2000
        y = 1100

        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        self.sign_up_frame.pack(pady=205)

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

        B = tk.Button(self.sign_up_frame, text="OK - SIGN UP", bg="DarkBlue", font=sign_up_font,
                      fg='snow',
                      command=lambda: self.sign_up_database_stuff(email_entry, username_entry, password_entry))
        B.pack(side='left', padx=20, pady=20)

        back_home = tk.Button(self.sign_up_frame, text="BACK", bg="DarkBlue", font=sign_up_font,
                              fg='snow', command=self.back_from_sign_up)
        back_home.pack(side='right', padx=20, pady=20)

        self.root.title(f"SHARED PAINTER - SIGN UP")

        self.root.mainloop()

    def back_to_login(self):
        """
        The function returns to the login screen after going back to the home screen from the login screen.
        """
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

        self.root.title(f"SHARED PAINTER - LOGIN")

        self.root.mainloop()

    def back_from_login(self):
        """
        The function returns to the home screen from the login screen.
        """
        self.login_frame.pack_forget()
        self.back_to_initial_screen()

    def login_database_stuff(self, username_entry, password_entry):
        """
        The function sends a client's login information to the server,
        which logs it into the designated login database.
        :param username_entry: The client's username entry.
        :param password_entry: The client's password entry.
        """
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        print(entered_username)
        print(entered_password)

        self.current_username = entered_username

        can_continue = self.server.login(entered_username, entered_password)
        print("can? " + str(can_continue))

        if can_continue == "ok":
            self.login_code_screen()

        else:
            self.login_frame.pack_forget()
            self.back_to_login()

    def is_entered_code_ok(self, code_entry):
        """
        The function sends the client's entered code to the server, which checks whether the
        code is correct or not. If the code is correct, the canvas screen is displayed and
        the client's login process is complete. If the code is incorrect, the client is requested
        to re-enter it.
        :param code_entry: The client's code entry.
        """
        self.login_code_frame.pack_forget()
        self.code_incorrect_frame.pack_forget()

        login_code_font = ("Segoe Print", 20)
        bg_color = "#%02x%02x%02x" % (243, 249, 151)

        is_code_ok = self.server.is_login_code_ok(code_entry)

        if is_code_ok:
            self.design_canvas_screen()
            #self.server.clients_lst[0], self.server.clients_lst[1] = self.server.clients_lst[1], self.server.clients_lst[0]
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

    def login_code_screen(self):
        """
        The function creates the screen displayed to clients during logins, where
        they are requested to enter the code sent to their email address.
        """
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

    """FORGOT PASSWORD"""

    def continue_after_changing_password(self):
        """
        The function returns to the login screen after changing a client's password.
        """
        self.change_password_frame.pack_forget()
        self.back_to_login()

    def change_password(self, entered_username, password_entry):
        """
        The function sends a client's entered username and new password to the server, which
        updates the designated database.
        :param entered_username: The client's entered username.
        :param password_entry: The client's entered new password.
        """
        new_password = password_entry.get()

        print("This is the new password:")
        print(new_password)
        self.server.change_to_new_password(entered_username, new_password)

        self.continue_after_changing_password()

    def change_password_screen(self, entered_username):
        """
        The function creates the second screen displayed to clients when they click "forgot password",
        which they see if the username they entered is in the designated database. In this screen,
        the clients are requested to enter a new password.
        :param entered_username: The client's entered username.
        """
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

        B = tk.Button(self.change_password_frame, text='Continue', bg="DarkBlue", font=login_font, fg='snow',
                      command=lambda: self.change_password(entered_username, password_entry))
        B.pack()

        self.root.title(f"SHARED PAINTER - FORGOT PASSWORD")

    def check_and_change_password(self, username_entry):
        """
        The function sends the username a client entered to the server, which checks whether it's
        in the designated database or not. If the username is in the database, the client's password can be changed.
        If not, an error message is displayed and the client is requested to re-enter the username.
        :param username_entry: The client's username entry.
        """
        # self.sign_up_database.create_users_list()
        entered_username = username_entry.get()
        print(entered_username)

        can_change_password = self.server.check_to_change_password(entered_username)

        if can_change_password:
            self.change_password_screen(entered_username)

        else:
            tk.messagebox.showerror(title="ERROR",
                                    message="The username you entered does not exist in the system.\n"
                                            + "Please try again.")
            self.forgot_password_frame.pack_forget()
            self.back_to_forgot_password_screen()

    def back_to_forgot_password_screen(self):
        """
        The function returns to the "forgot password" screen after going back to the login
        screen from the "forgot password" screen.
        """
        self.login_frame.pack_forget()
        self.forgot_password_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)
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

    def forgot_password_screen(self):
        """
        The function creates the first screen displayed to clients when they click "forgot password",
        where they enter their username.
        """
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

    """FORGOT PASSWORD"""

    def design_login_screen(self):
        """
        The function creates the main screen used during logins.
        """
        self.initial_frame.pack_forget()

        x = 2000
        y = 1100

        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        self.root.title(f"SHARED PAINTER - LOGIN")

        self.login_frame.pack(pady=250)

        login_font = ("Segoe Print", 15)

        username_label = tk.Label(self.login_frame, text="Username: ", bg=bg_color, font=login_font)
        username_label.pack()
        username_entry = tk.Entry(self.login_frame, font=login_font)
        username_entry.pack(pady=10)

        password_label = tk.Label(self.login_frame, text="Password: ", bg=bg_color, font=login_font)
        password_label.pack()
        password_entry = tk.Entry(self.login_frame, show="*", font=login_font)
        password_entry.pack(pady=10)

        B = tk.Button(self.login_frame, text="OK - LOGIN", bg="DarkBlue", font=login_font, fg='snow',
                      command=lambda: self.login_database_stuff(username_entry, password_entry))
        B.pack(side='left', padx=20, pady=20)

        back_home = tk.Button(self.login_frame, text="BACK", bg="DarkBlue",
                              font=login_font, fg='snow', command=self.back_from_login)
        back_home.pack(padx=20, pady=20, anchor='center')

        forgot_password_button = tk.Button(self.login_frame, text="Forgot" + "\n" + "Password", bg="DarkBlue",
                                           font=login_font, fg='snow', command=self.forgot_password_screen)
        forgot_password_button.pack(side='right', padx=20, pady=20)

        self.root.mainloop()

    def back_from_about_us(self):
        """
        The function returns to the home screen from the "about us" screen.
        """
        self.about_us_frame.pack_forget()
        self.back_to_initial_screen()

    def back_to_about_us(self):
        """
        The function returns to the "about us" screen after going back to the home screen from the "about us" screen.
        """
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

        # about_us_text = """Shared Painter has a simple purpose: building connections between people.
        # This goal is obtained by using art to encourage collaboration between individuals, showing
        # that despite our differences, together we can create great things.
        #
        # Simply choose a color, a brush size, and draw away! You will be sharing a canvas with other
        # users and painting on it simultaneously, eventually producing a one-of-a-kind masterpiece."""
        #
        # about_us_label = tk.Label(self.about_us_frame, text=about_us_text, bg=bg_color, font=("Segoe Print", 15))
        # about_us_label.pack(pady=150, anchor='center')

        about_us_text = "Shared Painter has a simple purpose: building connections between people." + "\n" + \
                        "This goal is obtained by using art to encourage collaboration between individuals," + "\n" + \
                        "showing that despite our differences, together we can create great things." + "\n" + "\n" + \
                        "Simply choose a color, a brush size, and draw away!" + "\n" + "You will be sharing a canvas " \
                        "with other users and painting on it simultaneously," + "\n" + "eventually producing a " \
                        "one-of-a-kind masterpiece."

        about_us_label = tk.Label(self.about_us_frame, text=about_us_text, bg=bg_color, font=("Segoe Print", 19))
        about_us_label.pack(side=tk.TOP, pady=170, anchor='center')

        back_home = tk.Button(self.about_us_frame, text="BACK", bg="DarkBlue", font=("Segoe Print", 16),
                              fg='snow', width=7, command=self.back_from_about_us)
        back_home.pack()

        self.root.mainloop()

    def design_about_us_screen(self):
        """
        The function creates the information screen displayed when the "about us"
        button is pressed.
        """
        self.initial_frame.pack_forget()

        x = 2000
        y = 1100

        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        self.root.title(f"SHARED PAINTER - ABOUT US")

        self.about_us_frame.pack(pady=20)

        # about_us_text = """Shared Painter has a simple purpose: building connections between people.
        # This goal is obtained by using art to encourage collaboration between individuals, showing
        # that despite our differences, together we can create great things.
        #
        # Simply choose a color, a brush size, and draw away! You will be sharing a canvas with other
        # users and painting on it simultaneously, eventually producing a one-of-a-kind masterpiece."""

        about_us_text = "Shared Painter has a simple purpose: building connections between people." + "\n" +\
                        "This goal is obtained by using art to encourage collaboration between individuals," + "\n" +\
                        "showing that despite our differences, together we can create great things." + "\n" + "\n" +\
                        "Simply choose a color, a brush size, and draw away!" + "\n" + "You will be sharing a canvas " \
                        "with other users and painting on it simultaneously," + "\n" + "eventually producing a " \
                        "one-of-a-kind masterpiece."

        about_us_label = tk.Label(self.about_us_frame, text=about_us_text, bg=bg_color, font=("Segoe Print", 19))
        about_us_label.pack(side=tk.TOP, pady=170, anchor='center')
        # about_us_label.pack(padx=10, pady=120)

        back_home = tk.Button(self.about_us_frame, text="BACK", bg="DarkBlue", font=("Segoe Print", 16),
                              fg='snow', width=7, command=self.back_from_about_us)
        back_home.pack()

        self.root.mainloop()


    def back_from_gallery_screen(self):
        """
        The function returns to the home screen from the gallery screen.
        """
        self.main_frame.pack_forget()
        self.my_canvas.pack_forget()
        self.back_to_initial_screen()


    def back_to_gallery_screen(self):
        """
        This function returns to the gallery screen after going back to the home screen
        from the gallery screen.
        """
        directory = r'Downsized_Cropped_Screenshots'

        # root = tk.Tk()
        # x = 2000
        # y = 1100
        # root.geometry("%dx%d" % (x, y))

        self.initial_frame.pack_forget()

        x = 2000
        y = 1100

        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        self.root.title(f"SHARED PAINTER - GALLERY")

        # Create a frame
        self.main_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100,
                                   width=2000)
        self.main_frame.pack(fill=tk.BOTH, expand=1)


        # Create a canvas
        self.my_canvas = tk.Canvas(self.main_frame, bg=bg_color)
        self.my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add a scrollbar to the canvas
        self.my_scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.gallery_back_home = tk.Button(self.my_canvas, text="BACK", bg="DarkBlue", font=("Segoe Print", 16),
                              fg='snow', command=self.back_from_gallery_screen)
        self.gallery_back_home.pack(side=tk.RIGHT, padx=50, pady=20, anchor="nw")

        # Configure the canvas
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Create ANOTHER frame INSIDE the canvas
        second_frame = tk.Frame(self.my_canvas, bg=bg_color)

        # Add that new frame to a window in the canvas
        self.my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        column_index = 0
        row_index = 0

        for filename in os.listdir(directory):
            # path = "trial_imgs" + r"'\'" + filename
            path = "Downsized_Cropped_Screenshots" + r"'\'" + filename
            path = path.replace("'", "")
            print(path)
            img = ImageTk.PhotoImage(Image.open(path))
            panel = tk.Label(second_frame, image=img)
            panel.image = img
            panel.grid(column=column_index, row=row_index, pady=20, padx=70)
            img_name = filename.replace("_small_", " ")
            img_name = img_name.replace(".png", "")
            lbl = tk.Label(second_frame, text=img_name, bg=bg_color, font=("Segoe Print", 12), fg="DarkBlue")
            lbl.grid(column=column_index, row=row_index + 1, pady=20, padx=70)

            if column_index < 3:
                column_index += 1

            if column_index >= 3:
                row_index += 2
                column_index = 0


    def design_gallery_screen(self):
        """
        This function designs the gallery screen displayed when the "gallery" button is pressed,
        where all saved drawings are displayed.
        """
        # directory = r'trial_imgs'
        directory = r'Downsized_Cropped_Screenshots'

        # root = tk.Tk()
        # x = 2000
        # y = 1100
        # root.geometry("%dx%d" % (x, y))

        self.initial_frame.pack_forget()

        x = 2000
        y = 1100

        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        self.root.title(f"SHARED PAINTER - GALLERY")

        # Create a frame
        self.main_frame.pack(fill=tk.BOTH, expand=1)


        # Create a canvas
        self.my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add a scrollbar to the canvas
        self.my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.gallery_back_home.pack(side=tk.RIGHT, padx=50, pady=20, anchor="nw")

        # Configure the canvas
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Create ANOTHER frame INSIDE the canvas
        second_frame = tk.Frame(self.my_canvas, bg=bg_color)


        # Add that new frame to a window in the canvas
        self.my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        column_index = 0
        row_index = 0

        for filename in os.listdir(directory):
            #path = "trial_imgs" + r"'\'" + filename
            path = "Downsized_Cropped_Screenshots" + r"'\'" + filename
            path = path.replace("'", "")
            print(path)
            img = ImageTk.PhotoImage(Image.open(path))
            panel = tk.Label(second_frame, image=img)
            panel.image = img
            panel.grid(column=column_index, row=row_index, pady=20, padx=70)
            img_name = filename.replace("_small_", " ")
            img_name = img_name.replace(".png", "")
            lbl = tk.Label(second_frame, text=img_name, bg=bg_color, font=("Segoe Print", 12), fg="DarkBlue")
            lbl.grid(column=column_index, row=row_index + 1, pady=20, padx=70)

            if column_index < 3:
                column_index += 1

            if column_index >= 3:
                row_index += 2
                column_index = 0


    def design_initial_screen(self):
        """
        The function creates the app's home screen.
        """
        x = 2000
        y = 1100

        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        self.initial_frame.pack()

        # gallery_button = tk.Button(self.initial_frame, text="GALLERY", bg="DarkBlue", font=("Segoe Print", 10),
        #                             fg="snow", height=2, width=8, command=self.design_gallery_screen)
        # gallery_button.pack(side="right", pady=10)
        gallery_button_icon = ImageTk.PhotoImage(file="final_gallery_logo.png")
        gallery_button = tk.Button(self.initial_frame, image=gallery_button_icon, borderwidth=0, bg=bg_color, font=("Segoe Print", 10),
                                   fg="snow", command=self.design_gallery_screen)
        gallery_button.pack(side="right", pady=10)

        logo_photo = ImageTk.PhotoImage(Image.open('project_logo_png.png'))
        logo_label = tk.Label(self.initial_frame, image=logo_photo)
        logo_label.pack(pady=95)

        login_button = tk.Button(self.initial_frame, text="LOGIN", bg="DarkBlue", font=("Segoe Print", 14),
                                 fg="snow", height=2, width=12, command=self.design_login_screen)
        login_button.pack(padx=60, pady=100, side='left')

        sign_up_button = tk.Button(self.initial_frame, text="SIGN UP", bg="DarkBlue", font=("Segoe Print", 14),
                                   fg="snow", height=2, width=12, command=self.design_sign_up_screen)
        sign_up_button.pack(padx=60, pady=100, side='right')

        about_us_button = tk.Button(self.initial_frame, text="ABOUT US", bg="DarkBlue", font=("Segoe Print", 14),
                                    fg="snow", height=2, width=12, command=self.design_about_us_screen)
        about_us_button.pack(padx=60, pady=100, anchor='center')

        self.root.title(f"SHARED PAINTER - HOME")

        self.root.mainloop()

    def back_to_initial_screen(self):
        """
        The function returns to the app's home screen after displaying a different screen.
        """
        self.initial_frame = tk.Frame(self.root, bg="#%02x%02x%02x" % (243, 249, 151), height=1100, width=2000)

        self.initial_frame.pack()

        # gallery_button = tk.Button(self.initial_frame, text="GALLERY", bg="DarkBlue", font=("Segoe Print", 10),
        #                            fg="snow", height=2, width=8, command=self.design_gallery_screen)
        # gallery_button.pack(side="right", pady=10)
        gallery_button_icon = ImageTk.PhotoImage(file="final_gallery_logo.png")
        gallery_button = tk.Button(self.initial_frame, image=gallery_button_icon, borderwidth=0,
                                   bg="#%02x%02x%02x" % (243, 249, 151), font=("Segoe Print", 10),
                                   fg="snow", command=self.design_gallery_screen)
        gallery_button.pack(side="right", pady=10)

        logo_photo = ImageTk.PhotoImage(Image.open('project_logo_png.png'))
        logo_label = tk.Label(self.initial_frame, image=logo_photo)
        logo_label.pack(pady=70)

        login_button = tk.Button(self.initial_frame, text="LOGIN", bg="DarkBlue", font=("Segoe Print", 14),
                                 fg="snow", height=2, width=12, command=self.back_to_login)
        login_button.pack(padx=60, pady=100, side='left')

        sign_up_button = tk.Button(self.initial_frame, text="SIGN UP", bg="DarkBlue", font=("Segoe Print", 14),
                                   fg="snow", height=2, width=12, command=self.back_to_sign_up)
        sign_up_button.pack(padx=60, pady=100, side='right')

        about_us_button = tk.Button(self.initial_frame, text="ABOUT US", bg="DarkBlue", font=("Segoe Print", 14),
                                    fg="snow", height=2, width=12, command=self.back_to_about_us)
        about_us_button.pack(padx=60, pady=100, anchor='center')

        self.root.title(f"SHARED PAINTER - HOME")

        self.root.mainloop()

    # def chosen_size(self, sizes_slider, screen):
    #     """
    #     The function sets the client's chosen brush size as the current brush size.
    #     :param sizes_Lb: The brush size listbox created.
    #     """
    #     # chosen_value = sizes_Lb.curselection()[0] + 1
    #     # self.brush_sizes_lst.append(chosen_value)
    #
    #     chosen_value = sizes_slider.get()
    #     print("CHOSEN SIZE: " + str(chosen_value))
    #     self.brush_sizes_lst.append(chosen_value)
    #
    #     if self.brush_sizes_lst != []:
    #         self.brush_size = self.brush_sizes_lst[-1]
    #
    #     screen.destroy()
    #
    #
    # def choose_brush_size(self):
    #     """
    #     The function creates the brush sizes listbox, displaying the brush sizes the client
    #     can choose from to draw on the canvas.
    #     """
    #
    #     bg_color = "#%02x%02x%02x" % (243, 249, 151)
    #     screen_font = ("Segoe Print", 10)
    #
    #     screen = tk.Tk()
    #     screen.title("Brush Size")
    #     screen.config(bg=bg_color)
    #
    #     # sizes_Lb = tk.Listbox(screen)
    #     # sizes_Lb.bind('<<ListboxSelect>>', lambda x: self.chosen_size(sizes_Lb))
    #     # sizes_Lb.pack()
    #     #
    #     # for i in range(1, 21):
    #     #     sizes_Lb.insert(i, i)
    #
    #     sizes_slider = tk.Scale(screen, from_=1, to=10, orient=tk.HORIZONTAL, bg=bg_color,
    #                             length=200, width=30)
    #
    #     sizes_slider.pack()
    #
    #
    #     b = tk.Button(screen, text="OK", bg="DarkBlue", font=screen_font, fg="snow",
    #                   command= lambda: self.chosen_size(sizes_slider, screen))
    #     b.pack()
    #
    #     screen.mainloop()


    def get_chosen_brush_size(self, chosen_value):
        """
        The function sets the client's chosen brush size as the current brush size.
        :param chosen_value: The client's chosen brush size.
        """
        chosen_value = int(chosen_value)
        self.brush_sizes_lst.append(chosen_value)

        if self.brush_sizes_lst != []:
            self.brush_size = self.brush_sizes_lst[-1]


    # def chosen_type(self, types_Lb):
    #     """
    #     The function sets the client's chosen brush type as the current brush type.
    #     :param types_Lb: The brush type listbox created.
    #     """
    #     chosen_value_index = types_Lb.curselection()[0]
    #     if chosen_value_index == 0:
    #         chosen_value = '●'
    #
    #     elif chosen_value_index == 1:
    #         chosen_value = '*'
    #
    #     self.brush_types_lst.append(chosen_value)
    #     print(chosen_value)
    #
    #     if self.brush_types_lst != []:
    #         self.brush_type = self.brush_types_lst[-1]
    #
    # def choose_brush_type(self):
    #     """
    #     The function creates the brush type listbox, displaying the brush types the client
    #     can choose from to draw on the canvas.
    #     """
    #     screen = tk.Tk()
    #     screen.title("Brush Type")
    #
    #     types_Lb = tk.Listbox(screen)
    #     types_Lb.bind('<<ListboxSelect>>', lambda x: self.chosen_type(types_Lb))
    #     types_Lb.pack()
    #
    #     types_Lb.insert(1, "●")
    #     types_Lb.insert(2, "*")
    #
    #     screen.mainloop()

    def set_circle_brush(self):
        """
        The function sets the brush type to '●'.
        """
        self.brush_type = "●"

    def set_asterisk_brush(self):
        """
        The function sets the brush type to '*'.
        """
        self.brush_type = "*"

    def choose_color(self):
        """
        The function creates the color palette widget, displaying the colors and shades the
        client can choose from to draw on the canvas.
        """
        # variable to store hexadecimal code of color
        color_code = colorchooser.askcolor(title="Color Palette")
        self.color = color_code[1]
        self.root.config(cursor='pencil')
        self.canvas_label.config(cursor='pencil')
        print(color_code)

    def crop_saved_screenshot(self, image_path, coords, saved_location):
        """
        This function crops a given image.
        :param image_path: The path to the image to edit.
        :param coords: A tuple of x/y coordinates (x1, y1, x2, y2).
        :param saved_location: Path to save the cropped image.
        """
        image_obj = Image.open(image_path)
        cropped_image = image_obj.crop(coords)
        cropped_image.save(saved_location)
        # cropped_image.show()

    def save_drawing(self):
        """
        The function saves the user's drawing and sends a copy to their email.
        """
        self.server.update_screenshot_num()
        num = int(self.server.screenshot_num)
        num = num + 1
        num = str(num)
        print("NUM: " + num)
        drawing_screenshot = pyautogui.screenshot()
        screenshot_path = "Screenshots" + r"'\'" + self.current_username + "'s_screenshot_" +\
                          num + ".png"
        screenshot_path = screenshot_path.replace("'", "")
        drawing_screenshot.save(screenshot_path)

        cropped_screenshot_path = "Cropped_Screenshots" + r"'\'" + self.current_username + "'s_cropped_screenshot_" +\
                                  num + ".png"
        cropped_screenshot_path = cropped_screenshot_path.replace("'", "")
        # self.crop_saved_screenshot(screenshot_path, (410, 25, 1910, 1028), cropped_screenshot_path) #SCHOOL SIZE
        self.crop_saved_screenshot(screenshot_path, (460, 75, 1910, 1008), cropped_screenshot_path)

        # cropped_directory = "Cropped_Screenshots"
        #self.server.send_saved_screenshot(self.current_username, cropped_directory, self.saved_screenshot_num)


        self.server.send_saved_screenshot(self.current_username, cropped_screenshot_path)

        to_downsize = Image.open(cropped_screenshot_path)
        to_downsize = to_downsize.resize((311, 200), Image.ANTIALIAS)
        downsized_screenshot_path = "Downsized_Cropped_Screenshots" + r"'\'" + self.current_username +\
                                    "'s_small_screenshot_" + num + ".png"
        downsized_screenshot_path = downsized_screenshot_path.replace("'", "")
        to_downsize.save(downsized_screenshot_path, quality=95, optimize=True)

        # self.saved_screenshot_num += 1




    def log_out(self):
        """
        The function returns to the app's home screen after displaying the canvas screen.
        """
        # self.canvas_frame.pack_forget()
        # self.canvas_label.pack_forget()
        # self.login_code_frame.pack_forget()
        # self.server.delete_login(self.current_username)
        # self.canvas_frame.pack_forget()
        # self.canvas_label.pack_forget()
        # self.login_code_frame.pack_forget()
        # self.design_initial_screen()
        # slaves_list = self.root.pack_slaves()
        # print(slaves_list)



    def design_canvas_screen(self):
        """
        The function creates the app's canvas screen.
        """
        x = 2000
        y = 1100

        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        log_out_button = tk.Button(self.canvas_frame, text="X", bg="DarkBlue", font=("Segoe Print", 11),
                                        fg="snow", height=2, width=2, command=self.on_quit)
        log_out_button.pack(side='left')
        save_drawing_button = tk.Button(self.canvas_frame, text="Save", bg="DarkBlue",
                                        font=("Segoe Print", 11),
                                        fg="snow", height=1, width=7, command=self.save_drawing)

        save_drawing_button.pack(side='top')

        self.canvas_frame.pack(side=tk.LEFT)
        self.logo_label.photo = self.logo_photo
        self.logo_label.pack(pady=50)

        color_palate_button = tk.Button(self.canvas_frame, text="Color" + "\n" + "Palette", bg="medium violet red",
                                        font=("Segoe Print", 11),
                                        fg="snow", height=2, width=10, command=self.choose_color)
        color_palate_button.pack(padx=120, pady=20)

        sizes_slider_label = tk.Label(self.canvas_frame, text='Brush Size', font=("Segoe Print", 12),
                                      bg=bg_color, fg="DarkBlue")
        sizes_slider_label.pack()

        sizes_slider = tk.Scale(self.canvas_frame, from_=1, to=10, orient=tk.HORIZONTAL, bg=bg_color,
                                length=200, width=30, command=self.get_chosen_brush_size)

        sizes_slider.pack()

        eraser_button = tk.Button(self.canvas_frame, text="Eraser", bg="medium violet red", font=("Segoe Print", 11),
                                  fg="snow", height=1, width=8, command=self.set_color_as_eraser)
        eraser_button.pack(padx=120, pady=20)

        # brush_type_button = tk.Button(self.canvas_frame, text="Brush Type", bg="medium violet red",
        #                               font=("Segoe Print", 11),
        #                               fg="snow", height=2, width=5, command=self.choose_brush_type)
        # brush_type_button.pack(padx=120, pady=10)

        brush_types_label = tk.Label(self.canvas_frame, text='Brush Type', font=("Segoe Print", 12), bg=bg_color,
                                      fg="DarkBlue")
        brush_types_label.pack()

        circle_brush_button = tk.Button(self.canvas_frame, text="●", bg="medium violet red",
                                      font=("Segoe Print", 11),
                                      fg="snow", height=1, width=5, command=self.set_circle_brush)
        circle_brush_button.pack(side=tk.LEFT, padx=80, pady=20)

        asterisk_brush_button = tk.Button(self.canvas_frame, text="*", bg="medium violet red",
                                      font=("Segoe Print", 11),
                                      fg="snow", height=1, width=5, command=self.set_asterisk_brush)
        asterisk_brush_button.pack(side=tk.LEFT)

        # brush_size_button = tk.Button(self.canvas_frame, text="Brush Size", bg="medium violet red",
        #                               font=("Segoe Print", 11),
        #                               fg="snow", height=2, width=10, command=self.choose_brush_size)
        #
        # brush_size_button.pack(padx=120, pady=10)



        # brush_type_button1 = tk.Button(self.canvas_frame, text="●", bg="medium violet red",
        #                                font=("Segoe Print", 13),
        #                                fg="snow", height=1, width=4, command=self.set_brush_type_1)
        # # brush_type_button1.pack(padx=10, pady=10)
        # brush_type_button1.place(x=150, y=750)
        #
        # brush_type_button2 = tk.Button(self.canvas_frame, text="*", bg="medium violet red",
        #                                font=("Segoe Print", 13),
        #                                fg="snow", height=1, width=4, command=self.set_brush_type_2)
        # # brush_type_button2.pack(padx=10, pady=10)
        # brush_type_button2.place(x=250, y=750)

    def color_pixel(self, pos):
        """
        The function colors a single pixel in the given position on the canvas,
        in the current color used by the client.
        :param pos: The position of the pixel to be colored.
        """
        """Place pixel at pos=(x,y) on image, with color=(r,g,b)."""
        if not self.stop_drawing:
            x, y = pos
            self.photo.put(self.color, (x, y))

        else:
            pass

    def set_color_as_eraser(self):
        """
        The function sets the current used color to an eraser.
        """
        self.color = '#f0f0f0'
        self.root.config(cursor='@eraser.cur')
        self.canvas_label.config(cursor='@eraser.cur')

    def color_pixel_for_server(self, pixels):
        """
        The function colors a single pixel in the given position on the canvas,
        in the given color.
        :param pos: The position of the pixel to be colored.
        :param color: The color of the pixel to be colored.
        """
        try:
            for pixel_to_draw in pixels:
                color = pixel_to_draw[0]
                coord = pixel_to_draw[1]
                print("COOOOOOORD: " + str(coord))
                x, y = coord
                brush_size = pixel_to_draw[2]
                brush_type = pixel_to_draw[3]

                if brush_type == "●":
                    for i in range(x, x + brush_size):
                        for j in range(y, y + brush_size):
                            if x >= 0:
                                self.photo.put(color, (i, j))

                elif brush_type == "*":
                    for i in range(brush_size):
                        pixels_to_color = [(x, y), (x + i, y), (x + i, y + i), (x, y + i), (x - i, y), (x - i, y - i),
                                           (x, y - i)]
                        # Eliminate repetitions
                        pixels_to_color = list(set(pixels_to_color))
                        # Color and append to the positions list every pixel in the list
                        for pixel in pixels_to_color:
                            if x >= 0:
                                self.photo.put(color, pixel)

        except ValueError:
            print("GOODBYE")

    def update_positions_lst(self, coord):
        """
        The function updates the list of the colored pixels' positions on the canvas.
        :param coords: A pixel's position on the canvas.
        """
        self.positions_lst.append((self.color, coord, self.brush_size, self.brush_type))
        print("coord: " + str(coord))

    def detect_motion(self, event):
        """
        The function detects the client's mouse motion on the canvas and sends
        the respective positions, according to the client's chosen brush size and type,
        to the "color_pixel" function.
        :param event:
        """

        # if self.color == '#f0f0f0':
        #     self.cursor = 'heart'

        # x, y = pyautogui.position()[0] - 397, pyautogui.position()[1]
        #print("ROOT X: " + str(self.root.winfo_pointerx()))
        #print("ROOT Y: " + str(self.root.winfo_pointery()))
        x, y = event.x, event.y + 25
        #print("pag pos: " + str(pyautogui.position()[0]) + " ,while real pos: " + str(x))
        print("winfo x: " + str(self.root.winfo_pointerx()) + " ,while real x: " + str(x))
        actual_x = pyautogui.position()[0]
        if self.root.winfo_pointerx() > 400 and x >= 0:
            self.update_positions_lst((x, y))
        # Color all pixels according to the brush size
        if self.brush_type == "●":
            for i in range(x, x + self.brush_size):
                for j in range(y, y + self.brush_size):
                    if self.root.winfo_pointerx() > 400 and x >= 0:
                        self.color_pixel((i, j))
                    else:
                        pass

        elif self.brush_type == "*":
            for i in range(self.brush_size):
                pixels_to_color = [(x, y), (x + i, y), (x + i, y + i), (x, y + i), (x - i, y), (x - i, y - i),
                                   (x, y - i)]
                # Eliminate repetitions
                pixels_to_color = list(set(pixels_to_color))
                # Color and append to the positions list every pixel in the list
                for pixel in pixels_to_color:
                    if self.root.winfo_pointerx() > 400 and x >= 0:
                        self.color_pixel(pixel)

    def pause_drawing(self):
        """
        This function gives a sign to pause the drawing process.
        """
        self.stop_drawing = True

    def resume_drawing(self):
        """
        This function gives a sign to resume the drawing process.
        """
        self.stop_drawing = False

    def setup(self):
        """
        The function displays the app's home screen.
        """
        self.root.protocol("WM_DELETE_WINDOW", self.on_quit)
        self.design_initial_screen()

    def on_quit(self):
        """
        The function closes the app.
        """
        self.server.delete_login(self.current_username)
        self.server_socket.send(pickle.dumps(["disconnect"]))
        self.running = False
        self.root.destroy()
        # self.server.delete_login(self.current_username)

    def run(self):
        """
        The function calls the "run_canvas" function in order to display
        the app's canvas screen and detect motion.
        """
        self.run_canvas()
        self.root.mainloop()

    def run_canvas(self):
        """
        The function binds the motion detector and creates the canvas clients draw on.
        """
        self.root.bind('<B1-Motion>', self.gambit)
        # self.canvas_label = tk.Label(self.root, image=self.photo, cursor=self.cursor)
        self.canvas_label.pack()
        self.root.title(f"SHARED PAINTER - {self.current_username}")
        self.root.mainloop()

    def gambit(self, event):
        """
        This function runs the program.
        :param event: A variable to detect motion.
        """
        threading.Thread(target=self.detect_motion, args=(event,)).start()

if __name__ == "__main__":
    app = Screens()
    app.design_initial_screen()