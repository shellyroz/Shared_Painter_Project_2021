import os
import tkinter as tk
from PIL import ImageTk, Image

directory = r'Downsized_Cropped_Screenshots'
print(os.listdir(directory))

root = tk.Tk()
x = 2000
y = 1100
root.geometry("%dx%d" % (x, y))
bg_color = "#%02x%02x%02x" % (243, 249, 151)
root["background"] = bg_color

i = 0


for filename in os.listdir(directory):
    path = "Downsized_Cropped_Screenshots" + r"'\'" + filename
    path = path.replace("'", "")
    print(path)
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(root, image=img)
    panel.grid(column=0, row=i, padx=35, pady=20)
    i += 1

root.mainloop()

