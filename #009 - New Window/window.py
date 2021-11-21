from tkinter import *
import sys 
import os
sys.path.append(os.path.abspath("/home/eduardo/Documentos/GitHub/tkinter/#009 - New Window/screens"))
from screen import *

root = Tk()
root.title('Old Window')

openTopScreen()
root.mainloop()