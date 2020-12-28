import tkinter as tk
from Project_Canvas_Screen import CanvasScreen

canvas_obj = CanvasScreen()
canvas_obj.design_canvas_screen()
canvas_obj.run_canvas()

from tkinter import *
from tkinter import colorchooser


# Function that will be invoked when the
# button will be clicked in the main window
# def choose_color():
#     # variable to store hexadecimal code of color
#     color_code = colorchooser.askcolor()
#
#
# root = Tk()
# button = Button(root, text="Select Color", command=choose_color)
# button.pack()
# root.geometry("300x300")
# root.mainloop()

