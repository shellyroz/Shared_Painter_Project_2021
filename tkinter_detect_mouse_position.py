# Base code from https://www.codegrepper.com/code-examples/python/tracking+mouse+position+tkinter+python

import tkinter as tk
root = tk.Tk()

lst = []

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    lst.append((x, y))


root.bind('<Motion>', motion)
root.mainloop()
print(lst)
