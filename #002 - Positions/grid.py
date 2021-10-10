from tkinter import *

root = Tk()

lblHello = Label(root, text='Hello World')
lblMyName = Label(root, text='My name is Eduardo Araujo')
#lblSpace = Label(root, text='                      ')  A Hack to create space in screen

lblHello.grid(row=0, column=0)
#lblSpace.grid(row=1, column=1)
lblMyName.grid(row=1, column=2)

root.mainloop()