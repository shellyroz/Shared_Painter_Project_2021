import tkinter as tk

class CanvasScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SHARED PAINTER - CANVAS")
        self.photo = tk.PhotoImage(width=900, height=650)
        self.stop_drawing = False


    def design_canvas_screen(self):
        x = self.root.winfo_screenwidth()
        y = self.root.winfo_screenwidth()
        self.root.geometry("%dx%d" % (x, y))

        bg_color = "#%02x%02x%02x" % (243, 249, 151)
        self.root["background"] = bg_color


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
        label.grid()
        self.root.mainloop()