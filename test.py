# print("hi")
# print("jasmin the queennnnnn")

# from tkinter import *
#
# def show_values():
#     print(w1.get())
#
# master = Tk()
# w1 = Scale(master, from_=0, to=42)
# w1.pack()
#
# Button(master, text='Show', command=show_values).pack()
#
# mainloop()

'''SCREENSHOT'''

# from PIL import Image
#
# def crop(image_path, coords, saved_location):
#     """
#     @param image_path: The path to the image to edit
#     @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
#     @param saved_location: Path to save the cropped image
#     """
#     image_obj = Image.open(image_path)
#     cropped_image = image_obj.crop(coords)
#     cropped_image.save(saved_location)
#     cropped_image.show()
#
# if __name__ == '__main__':
#     image = 'colors.jpg'
#     crop(image, (10, 10, 500, 900), 'cropped_colors.jpg')

import tkinter as tk

def print_value(val):
    print(val)

root = tk.Tk()

scale = tk.Scale(orient='horizontal', from_=0, to=128, command=print_value)
scale.pack()

root.mainloop()
