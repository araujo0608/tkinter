# Positions #
Lets use the grid system (rows and collunms) 
You can see the image in this directory to understand better and the syntax is this:

~~~python
#yourWidget.grid(row, column)
lblHello = Label(root, text='Hello World')
lblMyName = Label(root, text='My name is Eduardo Araujo')
lblMessage.grid(row=0, column=0)
lblMyName.grid(row=1, column=0)
~~~

<strong>You may not know this, but Python is also object-oriented. We can simplify this code this way:</strong>

~~~python
#yourWidget.grid(row, column)
lblHello = Label(root, text='Hello World').grid(row=0, column=0)
lblMyName = Label(root, text='My name is Eduardo Araujo').grid(row=1, column=0)
~~~

## Define size of window ##
To define a default size for our window we need use the *geometry* method and *resizable* method:

~~~python
from tkinter import *
root = Tk()
root.geometry("350x350")#width x height
root.resizable(False, False)# height, width
root.mainloop()
~~~
