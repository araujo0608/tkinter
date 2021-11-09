from tkinter import  *


root = Tk()
root.title('Radio Buttons')

lblTitle = Label(root, text='CHOOSE AN OPTION BELOW', font='bold')
lblTitle.config(font=40)
lblTitle.pack()

radio_var = IntVar()

Radiobutton(root, text='Option1', variable=radio_var, value=1).pack()
Radiobutton(root, text='Option2', variable=radio_var, value=2).pack()
Radiobutton(root, text='Option3', variable=radio_var, value=3).pack()


root.mainloop()