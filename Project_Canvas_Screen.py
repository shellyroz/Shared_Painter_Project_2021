import tkinter as tk
from tkinter import colorchooser

class CanvasScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SHARED PAINTER - CANVAS")
        self.photo = tk.PhotoImage(width=900, height=720)
        self.stop_drawing = False


    def design_canvas_screen(self):
        x = self.root.winfo_screenwidth()
        y = self.root.winfo_screenwidth()
        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color

        # frame = tk.Frame(self.root, width=200, height=200, bg=bg_color)
        # frame.pack(side=tk.LEFT)
        color_palate_button = tk.Button(self.root, text="Color Palate", bg="medium violet red", fg="snow",
                                        height=2, width=10)
        # , command=colorchooser.askcolor()
        color_palate_button.place(x=10, y=10)
        color_palate_button.pack()

        brush_size_button = tk.Button(self.root, text="Color Palate", bg="medium violet red", fg="snow",
                                        height=2, width=10)
        brush_size_button.place(x=10, y=50)
        brush_size_button.pack()


    # global photo
    # photo = tk.PhotoImage(width=900, height=650)
    #
    # def build_canvas(self):
    #     photo.place(x=150, y=50)

    # global stop_drawing
    # stop_drawing = False

    def color_pixel(self, image, pos, color):
        """Place pixel at pos=(x,y) on image, with color=(r,g,b)."""
        if self.stop_drawing == False:
            r, g, b = color
            x, y = pos
            image.put("#%02x%02x%02x" % (r, g, b), (x, y))

        else:
            pass

    def detect_motion(self, event):
        x, y = event.x, event.y
        color = (0, 0, 255)

        self.color_pixel(self.photo, (x, y), color)
        self.color_pixel(self.photo, (x + 1, y), color)
        self.color_pixel(self.photo, (x, y + 1), color)
        self.color_pixel(self.photo, (x + 1, y + 1), color)
        self.color_pixel(self.photo, (x - 1, y), color)
        self.color_pixel(self.photo, (x - 1, y + 1), color)
        self.color_pixel(self.photo, (x - 1, y + 2), color)
        self.color_pixel(self.photo, (x, y + 2), color)
        self.color_pixel(self.photo, (x + 1, y + 2), color)


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
        # label.place(x=100, y=0)
        label.pack()
        self.root.mainloop()


# if __name__ == "__main__":
#     app = CanvasScreen()
#     app.run_canvas()
