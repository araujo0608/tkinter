from tkinter import *

root = Tk()
root.title('Checkbox')
root.geometry('300x300')

checkvalue = StringVar()

def showValue():
    lblValue = Label(root, text=checkvalue.get()).pack()


checkbox = Checkbutton(root, text='Hey check me', variable=checkvalue, onvalue='You selected!', offvalue='Not selected')
checkbox.deselect()
checkbox.pack()

btnClick = Button(root, text='Action', command=showValue)
btnClick.pack()



root.mainloop()