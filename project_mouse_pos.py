import tkinter as tk

class MousePos:
    def __init__(self):
        self.root = tk.Tk()
        self.mouse_pos_lst = []

    def get_mouse_positions(self, event):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))
        self.mouse_pos_lst.append((x, y))

    def run_positions(self):
        self.root.bind('<Motion>', self.get_mouse_positions)
        self.root.mainloop()
        return self.mouse_pos_lst

    def color_pixel(self, color, pos, image):
        r, g, b = color
        x, y = pos
        image.put("#%02x%02x%02x" % (r, g, b), (y, x))

    def color_mouse_pos(self, pos):
        photo = tk.PhotoImage(width=32, height=32)
        self.color_pixel(photo, pos, (255, 0, 0))
        label = tk.Label(self.root, image=photo)
        label.grid()
        self.root.mainloop()

