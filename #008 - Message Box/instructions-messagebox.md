# Message Box #

First we need import *messagebox* module:
~~~python
from tkinter import messagebox
~~~

There a quite few *messagebox* types that we will see:
<br>
<br>
**001 - showinfo("title", "message") -> a simple popup without user interation. Just to show some information**
~~~python
from tkinter import *
from tkinter import messagebox as msgbox
root = Tk()

msgbox.showinfo("My first popup", "Hey, this is my popup")

root.mainloop()
~~~

**002 - showwarning("title", "message") -> a simple popup without user interation. Just to show some warning message**
~~~python
from tkinter import *
from tkinter import messagebox as msgbox
root = Tk()

msgbox.showwarning("Be careful", "Hey, pay attention")

root.mainloop()
~~~

**003 - showerror("title", "message") -> a simple popup without user interation. Just to show some error message**
~~~python
from tkinter import *
from tkinter import messagebox as msgbox
root = Tk()

msgbox.showerror("Error", "Hey, you delete c:/System32 path")

root.mainloop()
~~~

**004 - askquestion("title", "message") -> a simple popup asking something, but now will appear a Yes and No button**

~~~python
from tkinter import *
from tkinter import messagebox as msgbox
root = Tk()

msgbox.askquestion("Error", "Hey, you want delete c:/System32 path?")

root.mainloop()
~~~

How we can know what the user clicked? It is easy, is just use a variable:
~~~python
response = msgbox.askquestion("Error", "Hey, you want delete c:/System32 path?")
lblResponse = Label(root, text=response).pack()
~~~
> Yes will return **yes**
> No will return **no**

**005 - askokcancel("title", "message") -> a simple popup asking something, but now will appear a Ok and Cancel button**
~~~python
from tkinter import *
from tkinter import messagebox as msgbox
root = Tk()

msgbox.askokcancel("Question", "Hey, you want delete c:/System32 path?")

root.mainloop()
~~~

How we can know what the user clicked? It is easy, is just use a variable:
~~~python
response = msgbox.askokcancel("Error", "Hey, you want delete c:/System32 path?")
lblResponse = Label(root, text=response).pack()
~~~
> Ok will return **1**
> Cancel will return **0**

**006 - askyesno("title", "message") -> a simple popup asking something, but now will appear a Yes and No button**
~~~python
from tkinter import *
from tkinter import messagebox as msgbox
root = Tk()

msgbox.askyesno("Question", "Hey, you want delete c:/System32 path?")

root.mainloop()
~~~

How we can know what the user clicked? It is easy, is just use a variable:
~~~python
response = msgbox.askokcancel("Error", "Hey, you want delete c:/System32 path?")
lblResponse = Label(root, text=response).pack()
~~~
> Yes will return **1**
> No will return **0**
