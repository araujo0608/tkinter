from tkinter import *
from numpy import prod

root = Tk()
root.title('calculator')

memory = []
ope = 'null'

# functions
def clear():
    e.delete(0, END)

def addNumber(number):
    number = float(number)
    e.insert(END, number)

def sumNumbers():
    global ope
    ope = 'sum'
    memory.append(float(e.get()))
    clear()


def subNumbers():
    global ope
    ope = 'sub'
    global acumulator
    memory.append(float(e.get()))
    clear()

def multNumbers():
    global ope
    ope = 'mult'
    memory.append(float(e.get()))
    clear()

def divNumbers():
    global ope
    ope = 'div'
    global acumulator
    memory.append(float(e.get()))
    clear()

def showResult():
    memory.append(float(e.get()))
    clear()

    #print(ope)
    if ope == 'sum':
        e.insert(0, sum(memory))
        memory.clear()
    elif ope == 'sub':
        acumulator = memory[0]
        for index in range(1, len(memory)):
            acumulator = acumulator - memory[index]
        e.insert(0, acumulator)
        memory.clear()
    elif ope == 'mult':
        e.insert(0, prod(memory))
        memory.clear()
    elif ope == 'div':
        acumulator = memory[0]
        for index in range(1, len(memory)):
            acumulator = acumulator / memory[index]
        e.insert(0, acumulator)
        memory.clear()




e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Creating buttons

btnSum = Button(root, text='+', padx=40, pady=20, command=sumNumbers)
btnSub = Button(root, text='-', padx=40, pady=20, command=subNumbers)
btnMult = Button(root, text='X', padx=40, pady=20, command=multNumbers)
btnDiv = Button(root, text='/', padx=40, pady=20, command=divNumbers)
btnEqual = Button(root, text='=', padx=40, pady=20, command=showResult)
btnClear = Button(root, text='CE', padx=40, pady=20, command=clear)
btnOption0 = Button(root, text='0', padx=40, pady=20, command=lambda: addNumber(0))
btnOption1 = Button(root, text='1', padx=40, pady=20, command=lambda: addNumber(1))
btnOption2 = Button(root, text='2', padx=40, pady=20, command=lambda: addNumber(2))
btnOption3 = Button(root, text='3', padx=40, pady=20, command=lambda: addNumber(3))
btnOption4 = Button(root, text='4', padx=40, pady=20, command=lambda: addNumber(4))
btnOption5 = Button(root, text='5', padx=40, pady=20, command=lambda: addNumber(5))
btnOption6 = Button(root, text='6', padx=40, pady=20, command=lambda: addNumber(6))
btnOption7 = Button(root, text='7', padx=40, pady=20, command=lambda: addNumber(7))
btnOption8 = Button(root, text='8', padx=40, pady=20, command=lambda: addNumber(8))
btnOption9 = Button(root, text='9', padx=40, pady=20, command=lambda: addNumber(9))

# Put the button on screen

btnOption7.grid(row=1, column=0)
btnOption8.grid(row=1, column=1)
btnOption9.grid(row=1, column=2)
btnClear.grid(row=1, column=3)

btnOption4.grid(row=2, column=0)
btnOption5.grid(row=2, column=1)
btnOption6.grid(row=2, column=2)
btnSum.grid(row=2, column=3)

btnOption1.grid(row=3, column=0)
btnOption2.grid(row=3, column=1)
btnOption3.grid(row=3, column=2)
btnSub.grid(row=3, column=3)

btnOption0.grid(row=4, column=0)
btnMult.grid(row=4, column=1)
btnDiv.grid(row=4, column=2)
btnEqual.grid(row=4, column=3)

root = mainloop()
