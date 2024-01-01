from tkinter import *
from PIL import ImageTk, Image
import sys
import os

root = Tk()
root.title("Welcome to Python Tkinter")
# root.wm_iconbitmap("icon.ico")

myImg = ImageTk.PhotoImage(Image.open("myPic.jpeg"))
my_label = Label(image=myImg)
my_label.pack()

button_quit = Button(root, text="Exit", command=root.quit,bg="blue",fg="white")
button_quit.pack()

root.mainloop()
