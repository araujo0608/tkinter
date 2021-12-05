# Using Database SQlite3 on Tkinter #

## Creating or Connecting a database ##

Create or connect a database is the same command: 

var = sqlite3.connect('yourdatabase.db')

~~~python
conn = sqlite3.connect('address_book.db')
~~~

## Cursor ##

We need create a cursor to perform SQL queries in db using the connection variable. 

var = conn.cursor()

~~~python
c = conn.cursor()
~~~

## Create a table ##

Here we will create our table with column and data type.

cursor_var.execute(''' CREATE TABLE address(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zip_code integer
)      
                ''')

~~~python
c.execute(""" CREATE TABLE address(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zip_code integer
)
                
                """)
~~~