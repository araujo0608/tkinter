from tkinter import *
from PIL import ImageTk, Image
import emoji

root = Tk()
root.iconbitmap('images/icon python.ico') #defining icon
root.title('Viewer App') #defining title

#defining images and their paths
img1 = ImageTk.PhotoImage(Image.open('images/nature1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('images/nature2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('images/nature3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('images/nature4.jpg'))
img5 = ImageTk.PhotoImage(Image.open('images/nature5.jpg'))
img6 = ImageTk.PhotoImage(Image.open('images/nature6.jpg'))

image_list = [img1, img2, img3, img4, img5, img6] #index: 0 to 5

#label to show image
lblImage = Label(image=img1)
lblImage.grid(row=0, column=0, columnspan=3)

#Buttons (back, exit, next)
btnBack = Button(root, text=emoji.emojize(':leftwards_arrow_with_hook:', use_aliases=True), font=10)
btnBack.grid(row=1, column=1)
root.mainloop()