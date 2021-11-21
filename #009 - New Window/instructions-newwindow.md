# New Window on Tkinter #

It's preety easy open a new window in Tkinter. We need to use Toplevel() e just run it.

~~~python
from tkinter import *

root = Tk()
root.title('Learn about Window')

top = Toplevel() #Here is the new window

root.mainloop()
~~~

*But how can i put things on this new screen?* Well, when we create widgets and components we usually reference the main screen by passing it in the first attribute. So just reference this new window instead of the main screen. For example:
~~~python
from tkinter import *

root = Tk()
root.title('Learn about Window')

top = Toplevel()
lblMessage = Label(top, text='Label in new window').pack() #In the new Window
lblMsg = Label(root, text='Just a Label').pack() # In old Window

root.mainloop()
~~~
