<h1>Positions</h1>
<p>Lets use the grid system (rows and collunms) </p>
<p>You can see the image in this directory to understand better and the syntax is this:</p>

```
#yourWidget.grid(row, column)

lblHello = Label(root, text='Hello World')
lblMyName = Label(root, text='My name is Eduardo Araujo')

lblMessage.grid(row=0, column=0)
lblMyName.grid(row=1, column=0)
```

<strong>You may not know this, but Python is also object-oriented. We can simplify this code this way:</strong>

```
#yourWidget.grid(row, column)

lblHello = Label(root, text='Hello World').grid(row=0, column=0)
lblMyName = Label(root, text='My name is Eduardo Araujo').grid(row=1, column=0)
```