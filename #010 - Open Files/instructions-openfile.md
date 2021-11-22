# How to Open Files in Tkinter #

First we need import *filedialog* module
~~~python
from tkinter import filedialog
~~~

Now, to import a file we need ask the user which file he wants to choose. For this, let's call a function *askopenfilename()* 
The function askopenfile will open a box screen for the user. But it have some parameters such as:
<br>
<br>
**initialdir** - when the box popup, what the initial directory. EX: initialdir="/images"
<br>
**title** - title of the box popup. EX: title="Choose your file"
<br>
**filetypes** - filetypes the user can see and choose, like png, jpg, gif, pdf, all files. The first parameters is the description of file and the second the type EX: filetypes(("all files", "*.*"))
EX2: filetypes(("png files", "png.*"), ("jpg files", "jpg.*"))

~~~python
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Open Files")

root.filename = filedialog.askopenfilename(initialdir="home/eduardo/imagens", title="Choose your file", filetypes=[("all files", "*.*"])

root.mainloop()
~~~

The content of variable root.filename is the directory of the file.
