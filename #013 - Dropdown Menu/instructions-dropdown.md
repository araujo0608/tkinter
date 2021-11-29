# Dropdown Menu #

To create a dropdown menu we need use a **variable** to receive the value. A **list** for menu. And use the constructor **OptionMenu**. Look the example.

OptionMenu(main window, your variable, *your list)

~~~python
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

dropmenu = OptionMenu(root, value, *fruits)
dropmenu.pack()

root.mainloop()
~~~