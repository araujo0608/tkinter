from tkinter import *

root = Tk()


# Button functions
def click():
    number = e.get()
    text_result = ''
    if number.alpha():
        text_result = 'type ONLY NUMBERS!'
    else:
        number = int(number)
        if number % 2 == 0:
            text_result = 'even'
        else:
            text_result = 'odd'

    text_result = text_result.upper()
    lblAnswer = Label(root, text=text_result, font='bold', fg='blue')
    lblAnswer.config(font=60)
    lblAnswer.pack()


lblTitle = Label(root, text='EVEN or ODD - program')
lblTitle.config(font=60)
lblTitle.pack()

lblMessageInput = Label(root, text='Type a number below:')
lblMessageInput.pack()

e = Entry(root, width=50, borderwidth=5, bg='white', fg='blue')
e.pack()

btnClick = Button(root, text='check', width=20, command=click)
btnClick.pack()

root = mainloop()
