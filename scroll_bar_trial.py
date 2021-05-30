import tkinter as tk
from tkinter import ttk

import os
from PIL import ImageTk, Image

directory = r'trial_imgs'
# directory = r'Downsized_Cropped_Screenshots'

root = tk.Tk()
x = 2000
y = 1100
root.geometry("%dx%d" % (x, y))

# Create a frame
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

# Create a canvas
my_canvas = tk.Canvas(main_frame)
my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create ANOTHER frame INSIDE the canvas
second_frame = tk.Frame(my_canvas)

# Add that new frame to a window in the canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

column_index = 0
row_index = 0

for filename in os.listdir(directory):
    path = "trial_imgs" + r"'\'" + filename
    # path = "Downsized_Cropped_Screenshots" + r"'\'" + filename
    path = path.replace("'", "")
    print(path)
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(second_frame, image=img)
    panel.image = img
    panel.grid(column=column_index, row=row_index, padx=35, pady=20)

    if column_index < 3:
        column_index += 1

    if column_index >= 3:
        row_index += 1
        column_index = 0


root.mainloop()

