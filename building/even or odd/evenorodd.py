from tkinter import *

root = Tk()

#Button functions
def click():
    pass

lblTitle = Label(root, text='Welcome to Even or Odd program')
lblTitle.config(font=60)
lblTitle.pack()

lblMessageInput = Label(root, text='Type a number below:')
lblMessageInput.pack()

e = Entry(root, width=50, borderwidth=5, bg='white', fg='blue')
e.pack()

btnClick = Button(root, text='Check', width=20)
btnClick.pack()

root = mainloop()

#number = int(input('type your age: '))
#if type(number) == int:
#    print(number)
#else:
#    print('error')
