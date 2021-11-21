from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Open Files")

root.filename = filedialog.askopenfilename(initialdir="home/eduardo/imagens/", title="Choose your file", filetypes=[("all files", "*.*")])

root.mainloop()
