from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Open Files")


def openfile():
	filename = filedialog.askopenfilename(initialdir="home/eduardo/imagens/", title="Choose your file", filetypes=[("all files", "*.*")])
	lblFile = Label(root, text=filename).pack() #return the directory
	
btnOpenFile = Button(root, text='browse', command=openfile).pack()
root.mainloop()