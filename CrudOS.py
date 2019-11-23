from tkinter import *
import tkinter as tk
import sqlite3
conn = sqlite3.connect('mibase.db')
print("Connection successfully done.")

# We create the form
win =  Tk()
win.geometry("800x800")
#We create tha menu
menubar= Menu(win)

def addEmploye():
    addE =  Tk()
    entry1 = tk.Entry(addE)
    entry2 = tk.Entry(addE)
    entry3 = tk.Entry(addE)
    # form
    label1=  tk.Label(addE, text="Input the ID:", font= ("Helvetica", 20)).grid(row=0, column=1)

    entry1.grid(row=0, column=6)
    id =  entry1.get()

    label2 = tk.Label(addE, text="Input the name:", font=("Helvetica", 20)).grid(row=1, column=1)
    entry2.grid(row=1, column=6)
    name = entry1.get()

    label3 = tk.Label(addE, text="Input the salary:", font=("Helvetica", 20)).grid(row=3, column=1)
    entry3.grid(row=3, column=6)
    salary = entry3.get()

    sql = "INSERT INTO trabajadores(ID, name, salary) VALUES (id, name, salary);"
    # cursor executes the sentence
    cursors.execute(sql)
    # Commit for saving changes
    conn.commit()
    print(cursors.rowcount, "Worker inserted ..")

    addE.mainloop()
def searchEmploye():
    seaE = Tk()
    # form
    entry = tk.Entry(seaE)
    label = tk.Label(seaE, text="Input the ID of the worker: ", font=("Helvetica", 20)).grid(row=0, column=1)
    clavicordio = entry.get()
    sql = "SELECT * FROM trabajadores(code, nombre, sueldo) WHERE ID =  clavicordio;"# sql sentence again
    cursors.execute(sql)
    conn.commit()
    print("Done update!")
    if cursors.rowcount == 0:
        label1 = tk.Label(seaE, text="Input the name:", font=("Helvetica", 20)).grid(row=1, column=1)
    seaE.mainloop()
def updateEmploye():
    uE = Tk()
    # form
    entry = tk.Entry(uE).grid(row=0, column=6)
    entry1 = tk.Entry(uE).grid(row=1, column=6)
    entry2 = tk.Entry(uE).grid(row=2, column=6)
    label = tk.Label(uE, text="Input the ID of the worker: ", font=("Helvetica", 20)).grid(row=0, column=1)
    clavicordio = entry.get()

    name = tk.Label(uE, text="Input the name of the worker: ", font=("Helvetica", 20)).grid(row=1, column=1)
    id = entry1.get()

    salary = tk.Label(uE, text="Input the salary of the worker: ", font=("Helvetica", 20)).grid(row=2, column=1)
    id = entry2.get()
    sql = "UPDATE Trabajadores Set name =  name, salary= sal WHERE ID = clavicordio;"    # sql sentence again
    cursors.execute(sql)
    conn.commit()
    print("Done update!")
    uE.mainloop()

def deleteEmploye():
    dE = Tk()
    # form
    label1 = tk.Label(dE, text="Input the ID of the worker: ", font=("Helvetica", 20)).grid(row=0, column=1)
    entry1 = tk.Entry(dE).grid(row=0, column=6)
    clavicordio = entry1.get()
    button = tk.Button(dE, text="Delete").grid(row=3, column=2)
    sql = "DELETE * FROM trabajadores WHERE ID = clavicordio;"
    cursors.execute(sql)
    conn.commit()
    dE.mainloop()
#Primer menú
filemenu = Menu(menubar, tearoff = 0)
#Define the menu's functions
cursors =conn.cursor()

filemenu.add_command(label= "Add", command="addEmploye")
filemenu.add_command(label= "Search", command="searchEmploye")
filemenu.add_command(label= "Update", command="updateEmploye")
filemenu.add_command(label= "Delete", command="deleteEmploye")
menubar.add_cascade(label="CRUD", menu=filemenu)

win.config(menu= menubar)

repmenu = Menu(menubar, tearoff = 0)
#Define the menu's functions

repmenu.add_command(label= "Screen", command="displayScreen")
repmenu.add_command(label= "PDF", command="exportPDF")
repmenu.add_command(label= "Report", command="idk")
repmenu.add_cascade(label="Reports", menu=repmenu)

exmenu = Menu(menubar, tearoff = 0)
#Define the menu's functions

exmenu.add_command(label= "About", command="quienesSomos")
exmenu.add_command(label= "Exit", command=win.quit())
exmenu.add_cascade(label="Info", menu=repmenu)

win.config(menu= menubar)

win.mainloop()