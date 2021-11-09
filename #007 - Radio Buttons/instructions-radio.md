# Radio Buttons

First we need create a variable and the specific type of value in this variable:
~~~python
myvar = IntVar()
~~~

Then, we can create the Radio Button:
~~~python
Radiobutton(root, text='Option1', variable=myvar, value=1).pack()
Radiobutton(root, text='Option2', variable=myvar, value=2).pack()
~~~

