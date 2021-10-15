from tkinter import *

root = Tk()
root.title('calculator')

#functions
def addNumber():
    pass
def sumNumbers():
    pass
def subNumbers():
    pass
def showResult():
    pass

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Creating buttons

btnSum = Button(root, text='+', padx=39, pady=20, command=sumNumbers)
btnSub = Button(root, text='-', padx=39, pady=20, command=subNumbers)
btnEqual = Button(root, text='=', padx=39, pady=20, command=showResult)
btnOption0 = Button(root, text='0', width=31, padx=30, pady=20, command=addNumber)
btnOption1 = Button(root, text='1', padx=40, pady=20, command=addNumber)
btnOption2 = Button(root, text='2', padx=40, pady=20, command=addNumber)
btnOption3 = Button(root, text='3', padx=40, pady=20, command=addNumber)
btnOption4 = Button(root, text='4', padx=40, pady=20, command=addNumber)
btnOption5 = Button(root, text='5', padx=40, pady=20, command=addNumber)
btnOption6 = Button(root, text='6', padx=40, pady=20, command=addNumber)
btnOption7 = Button(root, text='7', padx=40, pady=20, command=addNumber)
btnOption8 = Button(root, text='8', padx=40, pady=20, command=addNumber)
btnOption9 = Button(root, text='9', padx=40, pady=20, command=addNumber)


# Put the button on screen

btnOption7.grid(row=1, column=0)
btnOption8.grid(row=1, column=1)
btnOption9.grid(row=1, column=2)

btnOption4.grid(row=2, column=0)
btnOption5.grid(row=2, column=1)
btnOption6.grid(row=2, column=2)

btnOption1.grid(row=3, column=0)
btnOption2.grid(row=3, column=1)
btnOption3.grid(row=3, column=2)

btnSum.grid(row=2, column=3)
btnSub.grid(row=3, column=3)
btnEqual.grid(row=4, column=3)
btnOption0.grid(row=4, column=0, columnspan=3)



root = mainloop()