import tkinter as tk
from tkinter import font as tkfont
from PIL import Image
from Project_Canvas_Screen import CanvasScreen


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, AboutUsPage, SignInPage, SignUpPage, RandPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        about_us_button = tk.Button(self, text="About Us", bg="blue4", fg="snow", height=2, width=10,
                                    command=lambda: controller.show_frame("AboutUsPage"))
        about_us_button.pack(side="top", anchor="ne", padx=10, pady=10)

        my_logo = tk.PhotoImage(file="project_logo_png.png")
        logo_lbl = tk.Label(self, image=my_logo)
        logo_lbl.pack(side="top", pady=10)
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        sign_in_button = tk.Button(self, text="Sign In", bg="blue4", fg="snow", height=2, width=10,
                                   command=lambda: controller.show_frame("SignInPage"))
        sign_in_button.pack(anchor="center", padx=10, pady=10)

        sign_up_button = tk.Button(self, text="Sign Up", bg="blue4", fg="snow", height=2, width=10,
                                   command=lambda: controller.show_frame("SignUpPage"))
        sign_up_button.pack(anchor="center", padx=10, pady=10)


class AboutUsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        info_text = '''
                Shared Painter has a simple purpose: building connections between people.
                This goal is obtained by using art to encourage collaboration between individuals,
                showing that despite our differences, together we can create great things.

                Simply choose a color, a brush size, and draw away!
                You will be sharing a canvas with other users and painting on it simultaneously,
                eventually producing a one-of-a-kind masterpiece.

                *Please note that paintings are limited in time and in the number of participants.
                '''

        # label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label = tk.Label(self, text=info_text)
        label.pack(side="top", anchor="center", padx=120, pady=10)
        button = tk.Button(self, text="Go to the home page",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()


class SignInPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This is the sign in page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        email_label = tk.Label(self, text="Email: ")
        email_label.pack()
        email_entry = tk.Entry(self)
        email_entry.pack(pady=10)
        # email_label.grid(row=0, column=0)
        # email_entry.grid(row=0, column=1)

        username_label = tk.Label(self, text="Username: ")
        username_label.pack()
        username_entry = tk.Entry(self)
        username_entry.pack(pady=10)

        password_label = tk.Label(self, text="Password: ")
        password_label.pack()
        password_entry = tk.Entry(self)
        password_entry.pack(pady=10)

        button = tk.Button(self, text="Go to the home page",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()


class SignUpPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This is the sign up page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        email_label = tk.Label(self, text="Email: ")
        email_label.pack()
        email_entry = tk.Entry(self)
        email_entry.pack(pady=10)
        # email_label.grid(row=0, column=0)
        # email_entry.grid(row=0, column=1)

        username_label = tk.Label(self, text="Username: ")
        username_label.pack()
        username_entry = tk.Entry(self)
        username_entry.pack(pady=10)

        password_label = tk.Label(self, text="Password: ")
        password_label.pack()
        password_entry = tk.Entry(self)
        password_entry.pack(pady=10)

        verify_password_label = tk.Label(self, text="Verify Password: ")
        verify_password_label.pack()
        verify_password_entry = tk.Entry(self)
        verify_password_entry.pack(pady=10)

        button = tk.Button(self, text="Go to the home page",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()

        button = tk.Button(self, text="Go to the rand page",
                           command=lambda: controller.show_frame("RandPage"))
        button.pack()


class RandPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # self.app1 = CanvasScreen()

        # canvas_obj = CanvasScreen()
        # canvas_obj.run_canvas()
        label = tk.Label(self, text="This is the rand page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Go to the sign up page",
                           command=lambda: controller.show_frame("SignUpPage"))
        button.pack()
        # self.app1.run_canvas()

#
# class RandPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#
#     def __init__1(self):
#         self.root = tk.Tk()
#         self.root.title("SHARED PAINTER - CANVAS")
#         self.photo = tk.PhotoImage(width=900, height=650)
#         self.stop_drawing = False
#
#
#     def color_pixel(self, image, pos, color):
#         """Place pixel at pos=(x,y) on image, with color=(r,g,b)."""
#         if self.stop_drawing == False:
#             r, g, b = color
#             x, y = pos
#             image.put("#%02x%02x%02x" % (r, g, b), (x, y))
#
#         else:
#             pass
#
#     def detect_motion(self, event):
#         x, y = event.x, event.y
#         color = (0, 0, 255)
#
#         self.color_pixel(self.photo, (x, y), color)
#         self.color_pixel(self.photo, (x + 1, y), color)
#         self.color_pixel(self.photo, (x, y + 1), color)
#         self.color_pixel(self.photo, (x + 1, y + 1), color)
#         self.color_pixel(self.photo, (x - 1, y), color)
#         self.color_pixel(self.photo, (x - 1, y + 1), color)
#         self.color_pixel(self.photo, (x - 1, y + 2), color)
#         self.color_pixel(self.photo, (x, y + 2), color)
#         self.color_pixel(self.photo, (x + 1, y + 2), color)
#
#
#     def pause_drawing(self, event):
#         self.stop_drawing = True
#
#
#     def resume_drawing(self, event):
#         self.stop_drawing = False
#
#     def run_canvas(self):
#         self.root.bind('<Motion>', self.detect_motion)
#         self.root.bind('<Button-1>', self.pause_drawing)
#         self.root.bind('<Button-3>', self.resume_drawing)
#         label = tk.Label(self.root, image=self.photo)
#         label.grid()
#         self.root.mainloop()







if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()