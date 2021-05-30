# import pyautogui
# #
# # my_screenshot = pyautogui.screenshot()
# # my_screenshot.save(r'Screenshots\screenshot1.png')
#
# screenshot_path = 'Screenshots' + r"'\'" + 'paint' + '.png'
# screenshot_path = screenshot_path.replace("'", "")
#
# my_screenshot = pyautogui.screenshot()
# my_screenshot.save(screenshot_path)
#
# print(screenshot_path)

from PIL import ImageTk, Image
import tkinter as tk

root = tk.Tk()
root.config(bg="DarkBlue")

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

frame1.pack(side=tk.LEFT)
frame2.pack(side=tk.RIGHT)

photo1 = ImageTk.PhotoImage(Image.open(r'small_project_logo_png.png'))
label1 = tk.Label(frame1, image=photo1)

photo2 = ImageTk.PhotoImage(Image.open(r'smiley_png.png'))
label2 = tk.Label(frame2, image=photo2)

label1.pack()
label2.pack()

root.mainloop()