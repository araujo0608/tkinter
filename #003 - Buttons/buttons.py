from tkinter import *

root = Tk()

#button function
def click():
    lblText = Label(root, text='Well, you clicked a Button', fg='red').pack()

btnClick = Button(root, text='Click me!', command=click, fg='blue', bg='orange').pack()

root.mainloop()