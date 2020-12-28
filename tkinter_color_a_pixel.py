import tkinter as tk
root = tk.Tk()

def pixel(image, pos, color):
    """Place pixel at pos=(x,y) on image, with color=(r,g,b)."""
    r,g,b = color
    x, y = pos
    image.put("#%02x%02x%02x" % (r,g,b), (y, x))


photo = tk.PhotoImage(width=32, height=32)

pixel(photo, (16, 16), (255, 0, 0))

label = tk.Label(root, image=photo)
label.grid()
root.mainloop()


