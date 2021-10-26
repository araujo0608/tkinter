from tkinter import *
from PIL import ImageTk, Image #importing modules for images

root = Tk()
root.title('Icons and Images')
root.iconbitmap('icon python.ico')

my_img = ImageTk.PhotoImage(Image.open("tkinter-image.jpg"))
lblMyImage = Label(image=my_img)
lblMyImage.pack()


#root.quit just quit the program
btnExit = Button(root, text='Exit program', command=root.quit, padx=15, pady=15)
btnExit.pack()

root = mainloop()