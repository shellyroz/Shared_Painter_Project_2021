import tkinter as tk
from tkinter import *
from Project_Canvas_Screen import CanvasScreen
from Project_Home_Screen import HomeScreen

class Screen:
    def __init__(self):
        self.obj1 = CanvasScreen()
        self.obj2 = HomeScreen()

        self.obj1.design_canvas_screen()
        self.obj1.run_canvas()

    # def run_screens(self):
    #     self.obj1.design_canvas_screen()
    #     self.obj1.run_canvas()


sc = Screen()
sc.run_screens()
