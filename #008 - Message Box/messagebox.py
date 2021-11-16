from tkinter import *
from tkinter import messagebox as msgbox


root = Tk()
root.title('Message Box')


r = msgbox.askquestion("Error", "Hey, you want delete c:/System32 path?")
lblR = Label(root, text=r).pack()

root.mainloop()