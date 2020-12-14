import tkinter as tk
root = tk.Tk()

# photo = tk.PhotoImage(width=1280, height=720)
photo = tk.PhotoImage(file="white_background_png.png")

global stop_drawing
stop_drawing = False


def pixel(image, pos, color):
    """Place pixel at pos=(x,y) on image, with color=(r,g,b)."""
    if stop_drawing == False:
        r, g, b = color
        x, y = pos
        image.put("#%02x%02x%02x" % (r, g, b), (x, y))

    else:
        pass



def motion(event):
    x, y = event.x, event.y
    color = (0, 0, 255)

    # print('{}, {}'.format(x, y))
    # lst.append((x, y))
    pixel(photo, (x, y), color)
    pixel(photo, (x + 1, y), color)
    pixel(photo, (x, y + 1), color)
    pixel(photo, (x + 1, y + 1), color)
    pixel(photo, (x - 1, y), color)
    pixel(photo, (x - 1, y + 1), color)
    pixel(photo, (x - 1, y + 2), color)
    pixel(photo, (x, y + 2), color)
    pixel(photo, (x + 1, y + 2), color)


def pause(event):
    global stop_drawing
    stop_drawing = True

def resume(event):
    global stop_drawing
    stop_drawing = False


root.bind('<Motion>', motion)
root.bind('<Button-1>', pause)
root.bind('<Button-3>', resume)
label = tk.Label(root, image=photo)
label.grid()
root.mainloop()



# photo = tk.PhotoImage(width=32, height=32)
#
# for i in range(len(lst)):
#     pixel(photo, (lst[i]), (255, 0, 0))


