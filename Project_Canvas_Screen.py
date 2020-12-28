import tkinter as tk
from tkinter import colorchooser
from functools import partial

class CanvasScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SHARED PAINTER - CANVAS")
        self.photo = tk.PhotoImage(width=900, height=720)
        self.color = "#000000"
        self.brush_sizes_lst = []
        self.brush_size = 1
        self.stop_drawing = False

    # Function that will be invoked when the
    # button will be clicked in the main window

    def chosen_size(self, sizes_Lb):
        chosen_value = sizes_Lb.curselection()[0] + 1
        self.brush_sizes_lst.append(chosen_value)

        if self.brush_sizes_lst[0] != None:
            self.brush_size = self.brush_sizes_lst[-1]



    def choose_brush_size(self):
        screen = tk.Tk()
        screen.title("Brush Size")

        sizes_Lb = tk.Listbox(screen)
        sizes_Lb.bind('<<ListboxSelect>>', lambda x: self.chosen_size(sizes_Lb))
        sizes_Lb.pack()

        sizes_Lb.insert(1, 1)
        sizes_Lb.insert(2, 2)
        sizes_Lb.insert(3, 3)
        sizes_Lb.insert(4, 4)

        screen.mainloop()


    def design_canvas_screen(self):
        x = self.root.winfo_screenwidth()
        y = self.root.winfo_screenwidth()
        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color


        def choose_color():
            # variable to store hexadecimal code of color
            color_code = colorchooser.askcolor(title="Color Palette")
            self.color = color_code[1]
            print(color_code)



        frame = tk.Frame(self.root, width=460, height=720, bg=bg_color)
        frame.pack(side=tk.LEFT)
        color_palate_button = tk.Button(frame, text="Color Palette", bg="medium violet red", fg="snow",
                                        height=2, width=10, command=choose_color)
        # color_palate_button.place(x=10, y=10)
        color_palate_button.pack(side=tk.LEFT, padx=10, pady=10)


        brush_size_button = tk.Button(frame, text="Brush Size", bg="medium violet red", fg="snow",
                                        height=2, width=10, command=self.choose_brush_size)
        # brush_size_button.place(x=10, y=80)
        brush_size_button.pack(side=tk.LEFT, padx=50, pady=80)


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
    def color_pixel(self, image, pos):
        """Place pixel at pos=(x,y) on image, with color=(r,g,b)."""
        if self.stop_drawing == False:
            x, y = pos
            image.put(self.color, (x, y))

        else:
            pass

    def detect_motion(self, event):
        x, y = event.x, event.y
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

        self.color_pixel(self.photo, (x, y))

        if self.brush_size == 2 or self.brush_size == 3 or self.brush_size == 4:
            self.color_pixel(self.photo, (x + 1, y))
            self.color_pixel(self.photo, (x, y + 1))
            self.color_pixel(self.photo, (x + 1, y + 1))

        if self.brush_size == 3 or self.brush_size == 4:
            self.color_pixel(self.photo, (x - 1, y))
            self.color_pixel(self.photo, (x - 1, y + 1))
            self.color_pixel(self.photo, (x - 1, y + 2))
            self.color_pixel(self.photo, (x, y + 2))
            self.color_pixel(self.photo, (x + 1, y + 2))

        if self.brush_size == 4:
            self.color_pixel(self.photo, (x + 2, y))
            self.color_pixel(self.photo, (x + 2, y + 1))
            self.color_pixel(self.photo, (x + 2, y + 2))
            self.color_pixel(self.photo, (x + 2, y + 3))
            self.color_pixel(self.photo, (x + 1, y + 3))
            self.color_pixel(self.photo, (x, y + 3))
            self.color_pixel(self.photo, (x - 1, y + 3))




        # self.color_pixel(self.photo, (x + 1, y))
        # self.color_pixel(self.photo, (x, y + 1))
        # self.color_pixel(self.photo, (x + 1, y + 1))
        # self.color_pixel(self.photo, (x - 1, y))
        # self.color_pixel(self.photo, (x - 1, y + 1))
        # self.color_pixel(self.photo, (x - 1, y + 2))
        # self.color_pixel(self.photo, (x, y + 2))
        # self.color_pixel(self.photo, (x + 1, y + 2))


    def pause_drawing(self, event):
        self.stop_drawing = True


    def resume_drawing(self, event):
        self.stop_drawing = False

    def run_canvas(self):
        self.root.bind('<Motion>', self.detect_motion)
        self.root.bind('<Button-1>', self.pause_drawing)
        self.root.bind('<Button-3>', self.resume_drawing)
        label = tk.Label(self.root, image=self.photo)
        # label.grid()
        label.place(x=100, y=0)
        label.pack()
        self.root.mainloop()


# if __name__ == "__main__":
#     app = CanvasScreen()
#     app.run_canvas()
