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
def insertInto():
    
    
    conn = sqlite3.connect('address_book.db')
    
    c = conn.cursor()
    
    conn.commit()

    conn.close()
    
    clear()