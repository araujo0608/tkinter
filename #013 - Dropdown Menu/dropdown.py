from tkinter import *

root = Tk()
root.title('Dropdown Menu')
root.geometry('300x300')


# List for Dropdown Menu
fruits = [
    'Banana',
    'Apple',
    'Avocato',
    'Strawberry',
    'Lemon'
    ]

# Variable to receive the selected option
value = StringVar()
value.set(fruits[0]) # Default selected option

def showSelectedDropMenu():
    lblShow = Label(root, text=value.get())
    lblShow.pack()

dropmenu = OptionMenu(root, value, *fruits)
dropmenu.pack()

btnClick = Button(root, text='show selected', command=showSelectedDropMenu)
btnClick.pack()

root.mainloop()