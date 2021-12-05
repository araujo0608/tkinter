from tkinter import *
import sqlite3

root = Tk()
root.title('Using Databases')
root.geometry('300x300')

# Creating or Connecting database
conn = sqlite3.connect('address_book.db')

# Creating cursor
c = conn.cursor()

c.execute("""CREATE TABLE address(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zip_code integer
)
                """)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()