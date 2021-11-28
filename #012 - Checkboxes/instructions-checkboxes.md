# Checkboxes #

To build a checkbox in tkinter, we need use *Checkbutton* constructor. But, before let's define a variable to receive the value. This values will be 0 or 1
~~~python
from tkinter import *

root = Tk()
root.title('Checkbox')
root.geometry('300x300')

checkvalue = IntVar()

checkbox = Checkbutton(root, text='Hey check me', variable=checkvalue)
checkbox.pack()

root.mainloop()
~~~

As said before, if the checkbox was selected then will return 1. If was not selected will return 0. *But how we can get the value?* It's just use *yourvar.get()* function

~~~python
from tkinter import *

root = Tk()
root.title('Checkbox')
root.geometry('300x300')

checkvalue = IntVar()

def showValue():
    lblValue = Label(root, text=checkvalue.get()).pack()


checkbox = Checkbutton(root, text='Hey check me', variable=checkvalue)
checkbox.pack()

btnClick = Button(root, text='Action', command=showValue)
btnClick.pack()



root.mainloop()
~~~

## Setting default value ##

We can just set a default value for checkbox using *onvalue* and *offvalue*

**onvalue=value** - when checkbox is selected will return a value pre-defined by you.

**offvalue=value** - when checkbox is **not** selected will return a value pre-defined by you.

~~~python
checkbox = Checkbutton(root, text='Hey check me', variable=checkvalue, onvalue='You selected!', offvalue='Not selected')
~~~
