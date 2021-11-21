from tkinter import *

def openTopScreen():
	top = Toplevel()
	top.title('My new window')
	lblMsg = Label(top, text='Click the button to exit').pack()
	btn = Button(top, text='close', command=top.destroy).pack()