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
index = 0

#label to show image
lblImage = Label(image=image_list[index])
lblImage.grid(row=0, column=0, columnspan=3)


#Functions
def back(indexn):
	global index
	global bntBack
	global lblImage

	if indexn == 0:
		index = 5
		lblImage.grid_forget()
		lblImage = Label(image=image_list[index])
		lblImage.grid(row=0, column=0, columnspan=3)
	else:
		index = index - 1
		lblImage.grid_forget()
		lblImage = Label(image=image_list[index])
		lblImage.grid(row=0, column=0, columnspan=3)





def forward(indexn):

	global index
	global btnNext
	global lblImage

	if indexn == 5:
		index = 0
		lblImage.grid_forget()
		lblImage = Label(image=image_list[index])
		lblImage.grid(row=0, column=0, columnspan=3)
	else:
		index = index + 1
		lblImage.grid_forget()
		lblImage = Label(image=image_list[index])
		lblImage.grid(row=0, column=0, columnspan=3)



#Buttons (back, exit, next)
btnBack = Button(root, text=emoji.emojize(':arrow_left:', use_aliases=True), font=10, command=lambda:back(index))
btnExit = Button(root, text='EXIT', font=10, command=root.quit)
btnNext = Button(root, text=emoji.emojize(':arrow_right:', use_aliases=True), font=10, command=lambda:forward(index))


#Puting the button on screen
btnBack.grid(row=1, column=1)	
btnExit.grid(row=1, column=2)
btnNext.grid(row=1, column=3)


root.mainloop()
