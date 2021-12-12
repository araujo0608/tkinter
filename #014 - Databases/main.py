from tkinter import *
import sqlite3

from functions import * # other file created by me

root = Tk()
root.title('Form for Users')
root.geometry('450x400')



# Creating or Connecting database
conn = sqlite3.connect('address_book.db')

# Creating cursor
c = conn.cursor()

'''
c.execute("""CREATE TABLE address(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zip_code integer
)
                """)
'''

# Labels in Grid
lblFirstname = Label(root, text='First Name: ')
lblLastname = Label(root, text='Last Name: ')
lblAddress = Label(root, text='Address: ')
lblCity = Label(root, text='City: ')
lblState = Label(root, text='State: ')
lblZipcode = Label(root, text='Zip-code: ')

lblFirstname.grid(row=0, column=0)
lblLastname.grid(row=1, column=0)
lblAddress.grid(row=2, column=0)
lblCity.grid(row=3, column=0)
lblState.grid(row=4, column=0)
lblZipcode.grid(row=5, column=0)


#Entrys in Grid

entryFirstname = Entry(root, width=30)
entryLastname = Entry(root, width=30)
entryAddress = Entry(root, width=30)
entryCity = Entry(root, width=30)
entryState = Entry(root, width=30)
entryZipcode = Entry(root, width=30)

entryFirstname.grid(row=0, column=1, columnspan=2)
entryLastname.grid(row=1, column=1, columnspan=2)
entryAddress.grid(row=2, column=1, columnspan=2)
entryCity.grid(row=3, column=1, columnspan=2)
entryState.grid(row=4, column=1, columnspan=2)
entryZipcode.grid(row=5, column=1, columnspan=2)

# Buttons in Grid

btnInsert = Button(root, text='Add to database')
btnShow = Button(root, text='Show database')

btnClear = Button(
    root, 
    text='Clear all fields', 
    command=lambda:clear(entryFirstname, entryLastname, entryAddress, entryCity, entryState, entryZipcode)
    )

btnClear.grid(row=0, column=3)
btnInsert.grid(row=6, column=0, columnspan=2)
btnShow.grid(row=7, column=0, columnspan=2)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()