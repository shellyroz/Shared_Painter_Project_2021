import tkinter as tk
from tkinter import messagebox

class HomeScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SHARED PAINTER")
        x = self.root.winfo_screenwidth()
        y = self.root.winfo_screenwidth()
        self.root.geometry("%dx%d" % (x,y))
        self.frame = tk.Frame(self.root, height=y, width=x)



    def info_box(self):
        box_title = "SHARED PAINTER - ABOUT US"
        box_info = '''Shared Painter has a simple purpose: building connections between people.
        This goal is obtained by using art to encourage collaboration between individuals,
        showing that despite our differences, together we can create great things.

        Simply choose a color, a brush size, and draw away!
        You will be sharing a canvas with other users and painting on it simultaneously,
        eventually producing a one-of-a-kind masterpiece.
        
        *Please note that paintings are limited in time and in the number of participants.
        '''
        messagebox.showinfo(box_title, box_info)

    def design_about_us_screen(self):
        self.root.destroy()
        self.root = tk.Tk()
        x = self.root.winfo_screenwidth()
        y = self.root.winfo_screenwidth()
        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        info_text = '''Shared Painter has a simple purpose: building connections between people.
        This goal is obtained by using art to encourage collaboration between individuals,
        showing that despite our differences, together we can create great things.

        Simply choose a color, a brush size, and draw away!
        You will be sharing a canvas with other users and painting on it simultaneously,
        eventually producing a one-of-a-kind masterpiece.
        
        *Please note that paintings are limited in time and in the number of participants.
        '''

        info_label = tk.Label(self.root, text=info_text)
        info_label.pack()

    def clear_screen(self):
        self.frame.pack_forget()


    def design_screen(self):
        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        clear_screen_button = tk.Button(self.frame, text='CLEAR', bg="blue4", fg="snow", height=2, width=10,
                                        command=self.clear_screen())
        clear_screen_button.pack()

        about_us_button = tk.Button(self.frame, text="About Us", bg="blue4", fg="snow", height=2, width=10)
        about_us_button.pack(side=tk.LEFT, anchor='ne', padx=10, pady=10)

        # my_logo = tk.PhotoImage(file="project_logo_png.png")
        # logo_lbl = tk.Label(self.root, image=my_logo)
        # logo_lbl.pack(anchor='center', pady=10)




        self.frame.pack()
        self.root.mainloop()


    def design_home_screen(self):
        x = self.root.winfo_screenwidth()
        y = self.root.winfo_screenwidth()
        self.root.geometry("%dx%d" % (x,y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        my_logo = tk.PhotoImage(file="project_logo_png.png")
        logo_lbl = tk.Label(self.root, image=my_logo)
        logo_lbl.pack()
        logo_lbl.place(x=400, y=100)

        about_us_button = tk.Button(self.root, text="About Us", bg="blue4", fg="snow", height=2, width=10,
                                    command=self.design_about_us_screen())
        about_us_button.place(x=1180, y=20)

        # about_us_button = tk.Button(self.root, text="About Us", bg="blue4", fg="snow", height=2, width=10)
        # about_us_button.place(x=1180, y=20)

        # sign_in_button = tk.Button(self.root, text="Sign In", bg="blue4", fg="snow", height=2, width=10, command=self.info_box())
        # sign_in_button.place(x=515, y=380)
        sign_in_button = tk.Button(self.root, text="Sign In", bg="blue4", fg="snow", height=2, width=10)
        sign_in_button.place(x=515, y=380)

        sign_up_button = tk.Button(self.root, text="Sign Up", bg="blue4", fg="snow", height=2, width=10)
        sign_up_button.place(x=655, y=380)



        self.root.mainloop()






