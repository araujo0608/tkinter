from tkinter import *

root = Tk()
root.title('Sliders')
root.geometry('300x500')

def showVertical():
	lblShow = Label(root, text="vertical: " + str(vertical.get()))
	lblShow.pack()

def showHorizontal():
	lblShow = Label(root, text="horizontal: " + str(horizontal.get()))
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