'''
 **PLEASE READ THE README FILE TO SEE INSTRUCTIONS**


 main.py - FGCU Data Engineering Internship DB Project
 Main file that houses the interface for our DB project.
 *WE ONLY HAVE A TEXT INTERFACE*

 Jason Knoll, Jordan Tatum, Chance Mullen

 Requirements:
 - A student can register to enter or search internships
 - A student must provide name and email address when registering
 - A student can provide an address and phone number when registering
 - A student does not have to have an internship as they may just register to search for internships
 - A new internship can be created without a student
 - An internship has 1 company
 - A company can have 1 or more internships 
 - There may be multiple instances of an internship by student and dates (start – end)
 - An instance of an internship must have 1 student
 - An internship must have at least one category, and can have multiple categories
 - A new internship instance should start with a copy of the internship categories 
'''

from typing import Optional
from sqlmodel import Field, SQLModel

import requests as r
import logging

# DB Models
# ------------------------------------------
'''
# Create our student table
class Student(SQLModel, table=True):
    student_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    address: Optional[str]
    phone: Optional[str]


# Officer Table
class Officer(SQLModel, table=True):
    officet_id: Optional[int] = Field(default=None, foreign_key="student.id")
    club_title: str
    name: str = Field(foreign_key="student.name")


class Company(SQLModel, table=True):
    pass


class Internship(SQLModel, table=True):
    pass


class Duties(SQLModel, table=True):
    pass
'''


# Interfacing
# ------------------------------------------
def query_menu():
    pass


def login_menu():
    '''Student enters their ID. The DB is queried to see if their ID is already registered'''
    print('Login =============')
    id = int(input('Enter your ID number: '))
    # check to see if they exist


def get_name(): 
    name = input('Enter your name: ')
    return name

def student_registration_menu():
    '''Student enters their information and is added to the DB'''

    print('Student Registration ============')

    name = ""

    while(name == ""): 
        name = get_name()
        if name == "":
            logging.warning("Name must not be empty")

    email = ""
    while(email == ""):
        email = input('Enter your email address: ')
        if email == "":
            logging.warning("Email must not be empty")


def main_menu(logged_in: bool):
    if logged_in == False:
        print("FGCU Student Internship DB =================")
        print("1. Student registration")
        print("2. Login (not real)")

        user = input()
        if user == "1":
            student_registration_menu()
        elif user == "2":
            login_menu()
    else:
        query_menu()


def main():
    main_menu(False)

    '''
    # idk try to get some response
    response = r.get('http://127.0.0.1:8000/3')
    print(response.json())
    '''


if __name__ == '__main__':
    main()
