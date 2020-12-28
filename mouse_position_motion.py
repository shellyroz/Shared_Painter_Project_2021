import tkinter as tk


def pixel(image, pos, color):
    """Place pixel at pos=(x,y) on image, with color=(r,g,b)."""
    r,g,b = color
    x, y = pos
    image.put("#%02x%02x%02x" % (r,g,b), (y, x))


def callback(event):
    p = (event.x, event.y)
    return p





root = tk.Tk()
bg_image = tk.PhotoImage(file="white_board.png")
lbl = tk.Label(root, image=bg_image)
lbl.pack()
lbl.bind("<Motion>", callback)
pixel(bg_image, (16, 16), (255, 0, 0))
root.mainloop()

