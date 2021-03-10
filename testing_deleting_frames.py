import tkinter as tk

root = tk.Tk()
bg_color = "#%02x%02x%02x" % (243, 0, 151)
root["background"] = bg_color

frame1 = tk.Frame(root)
frame1.pack()


def remove_frame1():
    frame1.destroy()
    frame2 = tk.Frame(root)
    frame2.pack()
    button2 = tk.Button(frame2, text='Hello')
    button2.pack()

removeB = tk.Button(frame1, text="Remove", width=10, command=remove_frame1)
removeB.pack()

root.mainloop()
