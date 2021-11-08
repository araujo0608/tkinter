from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Adding Frames')

frame = LabelFrame(root, text='This is my frame...', padx=5, pady=5)
frame.pack(padx=40, pady=40)

btnTest = Button(frame, text='dont click here!')
btnTest.pack()

root = mainloop()