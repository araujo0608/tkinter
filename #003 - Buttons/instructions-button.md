# Buttons
<p>Button is a widget too. Lets create a button:</p>

```python
#btn = Button(main widget, text='your text')
btnClick = Button(root, text='Click me!')
btnClick.pack()
```

*Change the size. In this case the atributes padx(axe X) and pady(axe Y) are used:*
```python
#btn = Button(main widget, text='your text', padx=value, pady=value)
btnClick = Button(root, text='Click me!', padx=20, pady=20)
btnClick.pack()
```
-----

### Setting event on click buttton
We need create a function that will be actived as soon as the button is clicked
```python
def click():
    #code...
```

In the button add this code:
```python
btnClick = Button(root, text='Click me!', command=your function)
```

Example:
```python
from tkinter import *

root = Tk()

#button function
def click():
    lblText = Label(root, text='Well, you clicked a Button').pack()

btnClick = Button(root, text='Click me!', command=click).pack()

root.mainloop()
```
