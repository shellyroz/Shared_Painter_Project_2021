import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
frame = tk.Frame(root, bg="#%02x%02x%02x" % (243, 249, 151), width=2000, height=1100)
frame.pack()

logo_photo = ImageTk.PhotoImage(Image.open('small_project_logo_png.png'))
logo_label = tk.Label(frame, image=logo_photo)
logo_label.pack(pady=50)

photo = tk.PhotoImage(width=1500, height=1100)
canvas_label = tk.Label(root, image=photo)
canvas_label.pack()



root.mainloop()