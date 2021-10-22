from tkinter import *

root = Tk()
root.title('Icons and Images')
root.iconbitmap('icon python.ico')
#root.quit just quit the program
btnExit = Button(root, text='Exit program', command=root.quit, padx=15, pady=15, fg='red')
btnExit.pack()

root = mainloop()