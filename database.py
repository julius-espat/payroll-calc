import sqlite3
import os.path
from sqlite3 import Error

def sql_connection():
    global con
    if os.path.isfile("payroll.db") != True:
        try:
            con = sqlite3.connect("payroll.db")

            print("Connection is established: Database has been created")
            
            cursor = con.cursor()

            cursor.execute("CREATE TABLE employees(ssnum text, firstname text,\
                middlename text,lastname text,\
                salary real, bonus integer,\
                terminated integer)")

            con.commit()

        except Error:

            print(Error)

    else:
        try:
            con = sqlite3.connect('payroll.db')

            print("Connection is established: Database has been loaded")

        except Error:

            print(Error)


