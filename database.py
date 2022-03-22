import sqlite3
import os.path
from sqlite3 import Error
import json
global con

def sql_connection(path):

    if path.endswith(".db") and os.path.exists(path):
        con = sqlite3.connect(path)

        print("Connection is established: Database has been loaded")
    else:
        raise ValueError('Path is incorrect')



def sql_generate(path):
    con = sqlite3.connect(path)

    print("Connection is established: Database has been created")

    cursor = con.cursor()

    cursor.execute("CREATE TABLE employees(fname text, mname text,\
            lname text, ssnum text,\
            init_date text, title text,\
            Address text, phone text,\
            birthday text, salary integer,\
            ss_discount_1 integer, ss_discount_2 integer,\
            ss_discount_employer_1 integer, ss_discount_employer_2 integer,\
            income integer, maritial_status text,\
            birth_country text, status integer,\
            document text, document_number text,\
            reference text, hours_per_week integer)")

    con.commit()