import tkinter as tk
from project_mouse_pos import MousePos

mouse_pos_object = MousePos()
lst = mouse_pos_object.run_positions()
print(lst)
for i in range(len(lst)):
    mouse_pos_object.color_mouse_pos(lst[i])


# def pixel(image, pos, color):
#     """Place pixel at pos=(x,y) on image, with color=(r,g,b)."""
#     r,g,b = color
#     x, y = pos
#     image.put("#%02x%02x%02x" % (r,g,b), (y, x))
#
# photo = tk.PhotoImage(width=32, height=32)
#
# for i in range(len(lst)):
#     pixel(photo, (lst[i]), (255, 0, 0))
#
# label = tk.Label(MousePos().root, image=photo)
# label.grid()
# mouse_pos_object.root.mainloop()