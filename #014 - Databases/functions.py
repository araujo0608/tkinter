from tkinter import *
import sqlite3

# This function clear all fields in form
def clear(entryFirstname, entryLastname, entryAddress, entryCity, entryState, entryZipcode):
    entryFirstname.delete(0, END)
    entryLastname.delete(0, END)
    entryAddress.delete(0, END)
    entryCity.delete(0, END)
    entryState.delete(0, END)
    entryZipcode.delete(0, END)

# This function add a record in db
def insertInto(entryFirstname, entryLastname, entryAddress, entryCity, entryState, entryZipcode):
    
    
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:firstname, :lastname, :address, :city, :state, :zip)", 
        {
            'firstname': entryFirstname,
            'lastname': entryLastname,
            'address': entryAddress,
            'city': entryCity,
            'state': entryState,
            'zip': entryZipcode
        }
    )

    conn.commit()
    conn.close()
    clear(entryFirstname, entryLastname, entryAddress, entryCity, entryState, entryZipcode)

# This function show database
def showDatabase(entryFirstname, entryLastname, entryAddress, entryCity, entryState, entryZipcode):

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    conn.commit()
    conn.close()
    clear(entryFirstname, entryLastname, entryAddress, entryCity, entryState, entryZipcode)