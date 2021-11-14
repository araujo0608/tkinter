from tkinter import  *


root = Tk()
root.title('Radio Buttons')


def showRadio():
	lblRadioSelection = Label(root, text=var_pizza.get()).pack()

lblTitle = Label(root, text='CHOOSE AN OPTION BELOW', font='bold')
lblTitle.config(font=40)
lblTitle.pack()

MODES = [
	("Pepperoni", "Pepperoni"), #text, value
	("Cheese", "Cheese"),
	("Mushroom", "Mushroom"),
	("Onion", "Onion"),
]

var_pizza = StringVar()

for text, value in MODES:
	Radiobutton(root, text=text, command=showRadio, variable=var_pizza, value=value).pack()

root.mainloop()