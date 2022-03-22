from ast import match_case
import PySimpleGUI as sg
from database import *
from commands import *


def simple_error(error_text):
    layout = [[sg.Text(error_text)],[sg.Button("Ok", key="ok")]]

    window = sg.Window("Error", layout)

    while True:
        event, values = window.read()
        if event == "ok" or event == sg.WIN_CLOSED:
            break
    window.close()


def database_select():
    layout = [[sg.Text("Please select database file: "), sg.FileBrowse(key="database",file_types=(("Database", ".db"),))],
    [sg.Button("Submit", key="submit")],[sg.Text("Enter Database to be created: "), sg.FileSaveAs(key="database2",file_types=(("Database", "*.db"),))],
    [sg.Button("Submit", key="submit2")]]

    window = sg.Window("Database Selection", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        if event == "submit":
            if values["database"].endswith(".db"):
                return values["database"] 
            else:
                window.close()
                simple_error("Please choose a proper database file")
        if event == "submit2":
            if values["database2"].endswith(".db"):
                sql_generate(values["database2"])
                window.close()
                return values["database2"] 
            else:
                simple_error("Please enter a proper database file")
        

def new_entry():
    left = [[sg.Text("Name (First, Middle Last)")], [sg.In(size=(25, 1), enable_events=True, key="fname"),sg.In(size=(25, 1), enable_events=True, key="mname"),sg.In(size=(25, 1), enable_events=True, key="lname")],
              [sg.Text("Social Security")], [sg.In(size=(25, 1), enable_events=True, key="ssnum")],
              [sg.Text("Permanent Address")], [sg.In(size=(25, 1), enable_events=True, key="ssnum")],
              [sg.Text("Phone Number")], [sg.In(size=(25, 1), enable_events=True, key="phone")],
              [sg.Text("Maritial Status")], [sg.In(size=(25, 1), enable_events=True, key="maritial_status")],
              [sg.Text("ID Document")], [sg.In(size=(25, 1), enable_events=True, key="document"),sg.Text("Number"),sg.In(size=(25, 1), enable_events=True, key="document_number")],
              [sg.Text("References")], [sg.In(size=(25, 1), enable_events=True, key="reference")],
              [sg.Text("Initial Date")], [sg.In(size=(25, 1), enable_events=True, key="init_date")],
              [sg.Text("Employment Status")], [sg.In(size=(25, 1), enable_events=True, key="status")],
              [sg.Button('Add',key="add_entry"),sg.Button('Cancel',key="cancel_entry")]]

    right = [[sg.Text("Salary Per Week")], [sg.In(size=(25, 1), enable_events=True, key="salary")],
            [sg.Text("Hours Per week")], [sg.In(size=(25, 1), enable_events=True, key="hours_per_week")],
            [sg.Text("Income Tax")], [sg.In(size=(25, 1), enable_events=True, key="income")],
            [sg.Text("Social S. Week 2")], [sg.In(size=(25, 1), enable_events=True, key="ss_discount_1")],
            [sg.Text("Social S. Week 1")], [sg.In(size=(25, 1), enable_events=True, key="ss_discount_2")],
            [sg.Text("Social S. Emp. Week 1")], [sg.In(size=(25, 1), enable_events=True, key="ss_discount_employer_1")],
            [sg.Text("Social S. Emp. Week 2")], [sg.In(size=(25, 1), enable_events=True, key="ss_discount_employer_2")]]

    layout = [[sg.Column(left, element_justification='l'), sg.Column(right, element_justification='c')]] 

    window = sg.Window("Employee Entry", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        
        if event == "add_entry":
            employee_init(values)
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
