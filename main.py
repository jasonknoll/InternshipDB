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

from typing import Optional, Any, Dict
from sqlmodel import Field, SQLModel, create_engine, Session

import requests as r
import logging


# Setup DB file to be read
sql_db_file = 'intern.db'
sqlite_url = f'sqlite:///{sql_db_file}'

engine = create_engine(sqlite_url, echo=True)

# DB Models
# ------------------------------------------


class Student(SQLModel, table=True):
    '''Create our student table'''

    student_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    address: Optional[str]
    phone: Optional[str]


'''
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

#


def insert_into_student(vars: Dict[str, Any]):
    pass


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Interfacing
# ------------------------------------------


def query_menu():
    print('Database ==============')
    print('1. Query database')
    print('2. Add database entry')


def login_menu():
    '''Student enters their ID. The DB is queried to see if their ID is already registered'''
    
    print('Login =============')
    id = int(input('Enter your ID number: '))
    # check to see if they exist


def student_registration_menu():
    '''Student enters their information and is added to the DB'''

    print('Student Registration ============')

    name = ""

    while(name == ""):
        name = input('Enter your name: ')
        if name == "":
            logging.warning("Name must not be empty!")

    email = ""
    while(email == ""):
        email = input('Enter your email address: ')
        if email == "":
            logging.warning("Email must not be empty!")

    address = input('Enter your address or press enter to leave blank: ')

    phone = input('Enter your phone number or press enter to leave blank: ')

    # Create student object
    s = Student(name=name, email=email, address=address, phone=phone)

    # Open a session with the DB
    sesh = Session(engine)

    # Add our model instance to the session
    sesh.add(s)

    # Commit the changes and store in DB
    sesh.commit()

    # Move onto the query menu
    query_menu()


def main_menu(logged_in: bool):
    if logged_in == False:
        print("FGCU Student Internship DB =================")
        print("1. Student registration")
        print("2. Student login (not actually)")
        print("3. Company registration")

        user = input()
        if user == "1":
            student_registration_menu()
        elif user == "2":
            login_menu()
    else:
        query_menu()


def main():
    create_db_and_tables()
    main_menu(False)

    '''
    # idk try to get some response
    response = r.get('http://127.0.0.1:8000/3')
    print(response.json())
    '''


if __name__ == '__main__':
    main()
