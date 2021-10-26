#Icons
<p> To download a icon visit iconarchive.com, choose an icon and download as .ico file</p>
<p>Sintax: [mainwindow].iconbitmap('directory of your .ico file')</p>
<p>Ex: root.iconbitmap('project/icons/myicon.ico')</p>
<br>

```
from tkinter import *
root = Tk()
root.iconbitmap('project/icons/myicon.ico')
root = mainloop()
```

#Images
<p>To use real images like JPEGs or PNG we have to import modules (Pillow) and do little things to make it happen</p>
<p>First we need install the package Pillow on terminal (if you use PyCharm is just add click in some buttons) with the command: pip install pillow</p>

```
from PIL import ImageTk, Image #importing modules
```

<p>Second: add your photo to a var. And put this var in other thing(Button, TextBox, Label...), and then put this otherthing in the screen</p>

```
my_img = ImageTk.PhotoImage(Image.open("directory/path of your image"))
lblMyImage = Label(image=my_img)
lblMyImage.pack()
```