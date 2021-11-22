# Sliders #

It's pretty simple use sliders. We just will use *Scale* method:
**from_** - initial value of slider
**to** - final value of slider
**orient=HORIZONTAL** - use this for horizontal slider

~~~python
from tkinter import *

root = Tk()
root.title('Sliders')
root.geometry('300x100')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

root.mainloop()
~~~

*But how can i get the value of slider?* Use vertical.get() or horizontal.get():

~~~python
from tkinter import *

root = Tk()
root.title('Sliders')
root.geometry('300x500')

def showVertical():
	lblShow = Label(root, text="vertical: " + str(vertical.get())) #get the value
	lblShow.pack()

def showHorizontal():
	lblShow = Label(root, text="horizontal: " + str(horizontal.get())) #get the value
	lblShow.pack()

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

btnShowVerticalSlider = Button(root, text='Show vertical value', command=showVertical)
btnShowVerticalSlider.pack()

btnShowHorizontalSlider = Button(root, text='Show horizontal value', command=showHorizontal)
btnShowHorizontalSlider.pack()

root.mainloop()
