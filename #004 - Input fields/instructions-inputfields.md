# Input Fields

<p>To add a input field in Tkinter, we need use the Entry() Widget</p>

Syntax, its pretty easy:
```
e = Entry(your main window, parametrers...)
e.pack()
```

Look the example below:

```
from tkinter import *
root = Tk()

e = Entry(root, width=50)
e.pack()

root.mainloop()
```

### Parametrers
* width -> width = 50
* bg -> bg = blue
* fg (font color) -> fg = white
* borderwidth -> borderwidth = 5
* and much more...

### Get the value
<p>For this we can use the get() function</p>

<p>Observer in the label on def click(), we called the e.get()</p>

```
from tkinter import *

root = Tk()

e = Entry(root, borderwidth=10, width=40)
e.pack()

#button function
def click():
    lblText = Label(root, text=e.get(), fg='red')
    lblText.pack()

btnClick = Button(root, text='Click me!', command=click, fg='blue', bg='orange')
btnClick.pack()

root.mainloop()
```
