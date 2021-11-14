# Radio Buttons #

First we need create a variable and the specific type of value in this variable:
~~~python
myvar = IntVar()
~~~

Then, we can create the Radio Button:
~~~python
Radiobutton(root, text='Option1', variable=myvar, value=1).pack()
Radiobutton(root, text='Option2', variable=myvar, value=2).pack()
~~~

Radio Button have *command* property like the Buttons. When you click, can call a function.
~~~python
def clicked01:
	print('do something...')

def clicked02:
	print('do another thing...')

Radiobutton(root, text='Option1', command=clicked01, variable=myvar, value=1).pack()
Radiobutton(root, text='Option2', command=clicked02, variable=myvar, value=2).pack()
~~~

Get value is so easy. Just use .get() function in that variable:
~~~python
lblRadioSelection = Label(root, text=myvar.get()).pack()
~~~

## Using loop to make a lot of Radios ##

it is important for you to know that it is possible to *make many radios through a loop*. This can be more **practical** and **faster**.

First we need create a list of tuples. First index in tuple is equivalent to the *text* property of Radio Button, and the second index is equivalent to the *value* property of Radio Button:

~~~python
def showRadio():
	lblRadioSelection = Label(root, text=var_pizza.get()).pack()

MODES = [
	("Pepperoni", "Pepperoni"), #text, value
	("Cheese", "Cheese"),
	("Mushroom", "Mushroom"),
	("Onion", "Onion"),
]

var_pizza = StringVar()

for text, value in MODES:
	Radiobutton(root, text=text, command=showRadio, variable=var_pizza, value=value).pack()
~~~