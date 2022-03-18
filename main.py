import PySimpleGUI as sg
import sqlite3
from database import *


def new_entry():
    con = sqlite3.connect("payroll.db")
    layout = [[sg.Text("Social Security")], [sg.In(size=(25, 1), enable_events=True, key="ssnum")],
              [sg.Text("First Name")], [sg.In(size=(25, 1), enable_events=True, key="fname")],
              [sg.Text("Middle Name")], [sg.In(size=(25, 1), enable_events=True, key="mname")],
              [sg.Text("Last Name")], [sg.In(size=(25, 1), enable_events=True, key="lname")],
              [sg.Text("Salary")], [sg.In(size=(25, 1), enable_events=True, key="salary")],
              [sg.Text("Additions")], [sg.In(size=(25, 1), enable_events=True, key="additions")],
              [sg.Button('Add',key="add_entry"),sg.Button('Cancel',key="cancel_entry")]]
    window = sg.Window("Employee Entry", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        
        if event == "add_entry":
            cursor = con.cursor()
            cursor.execute("INSERT INTO employees VALUES ('{}','{}','{}','{}',{},{},1)".format(values["ssnum"],values["fname"],
                       values["mname"],values["lname"],
                       values["salary"],values["additions"]))
            con.commit()
            break
        
        elif event == "cancel_entry" or event == sg.WIN_CLOSED:
            break
        
    window.close()
def main():
    layout = [[sg.Button("New Employee", key="new_entry")]]
    window = sg.Window("Main Window", layout, margins=(100,100))
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "new_entry":
            new_entry()
        
    window.close()
if __name__ == "__main__":
    sql_connection()
    main()