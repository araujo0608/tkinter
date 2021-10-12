from tkinter import *

root = Tk()

e = Entry(root, borderwidth=10, width=40)
e.pack()
e.insert(0, 'John') #default text in the field

#button function
def click():
    hello = 'Hello ' + e.get()
    lblText = Label(root, text=hello, fg='red')
    lblText.pack()

btnClick = Button(root, text='show my name', command=click, fg='blue', bg='orange')
btnClick.pack()

root.mainloop()