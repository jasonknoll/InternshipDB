'''
 **PLEASE READ THE README FILE TO SEE INSTRUCTIONS**


 main.py - FGCU Data Engineering Internship DB Project
 Main file that houses the interface for our DB project.
 *WE ONLY HAVE A TEXT INTERFACE*

 Jason Knoll, Jordan Tatum, Chance Mullen

'''

from typing import Optional, Any, Dict, Tuple
from sqlmodel import Field, SQLModel, create_engine, Session

import requests as r
import logging

# Setup DB file to be read
sql_db_file = 'intern.db'
sqlite_url = f'sqlite:///{sql_db_file}'

engine = create_engine(sqlite_url, echo=False)

# DB Models
# ------------------------------------------


class Student(SQLModel, table=True):
    '''Create our student table'''

    student_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    address: Optional[str]
    phone: Optional[str]

    # TODO create a view


class Officer(SQLModel, table=True):
    '''Officer table'''

    officer_id: Optional[int] = Field(
        default=None, primary_key=True, foreign_key="student.student_id")
    club_title: Optional[str]
    name: str = Field(default=None, foreign_key="student.name")


class Company(SQLModel, table=True):
    '''Company table'''

    company_name: str = Field(default=None, primary_key=True)
    address: Optional[str]
    email: Optional[str]


class Internship(SQLModel, table=True):
    '''Internship table'''

    internship_id: int = Field(default=None, primary_key=True)
    student_id: int = Field(default=None, foreign_key="student.student_id")
    company_name: str = Field(default=None, foreign_key="company.company_name")
    job_title: str
    dates: str
    wages: str
    status: str


class Duties(SQLModel, table=True):
    '''Duties table'''

    internship_id: int = Field(
        default=None, primary_key=True, foreign_key="internship.internship_id")
    title: Optional[str]
    experience: Optional[str]
    projects: Optional[str]


# C in CRUD
def insert_into(table: SQLModel, tuple: Tuple):
    pass


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Interfacing
# ------------------------------------------

# TODO finish the interface


def add_database_entry_menu():
    '''User enters their internship information and is added to the DB'''

    print('Internship Entry ============')            

    # Handle invalid inputs so the program doesn't crash
    company_name = ''
    while company_name == '':
        company_name = input("Enter the name of the company: ")
        if company_name == '':
            logging.warning("Please enter the company name.")

    internship_id = input("Enter the internship ID: ")

    student_id = input("Enter your student ID: ")
    
    job_title = input("Enter your job title at the internship or press enter to leave it blank: ")
    
    dates = input('Enter the dates spent at this internship or press enter to leave it blank: ')
 
    wages = input('Enter your wages at the internship or press enter to leave blank: ')

    status = input('Enter the status of your internship application or press enter to leave blank: ')       

    # Create internship object
    s = Internship(internship_id=internship_id, student_id=student_id, company_name=company_name, job_title=job_title, dates=dates, wages=wages, status=status)

    # Open a session with the DB
    sesh = Session(engine)

    # Add our model instance to the session
    sesh.add(s)

    # Commit the changes and store in DB
    sesh.commit()

    # Move onto the query menu
    db_menu()


def query_menu():
    pass


def db_menu():
    print('Database ==============')
    print('1. Query database')
    print('2. Add database entry')

    selection = input('> ')

    if selection == "1":
        query_menu()
    elif selection == "2":
        new_choice = ''
        while new_choice == '':
            print("1. Internship")
            print("2. Duties")
            new_choice = input("Which type of entry would you like to submit: ")
            if new_choice == '1':
                add_database_entry_menu()
            elif new_choice == "2":
                internship_id = input("Enter your internship's ID: ")
                duties_entry_menu(internship_id)
            else:
                logging.warning("Please enter a valid choice.")


def student_login():
    pass


def login_menu():
    '''Student enters their ID. The DB is queried to see if their ID is already registered'''

    print("Login ================")
    print("1. Student")
    print("2. Officer (must have student login)")
    print("3. Company")
    add_database_entry_menu() # Go to database entry because no login system is in place
    
    # TODO check to see if they exist already in the db to simulate a login


def company_register_menu():
    '''Company enters their information and is added to the DB'''

    print('Company Registration ============')

    # Handle invalid inputs so the program doesn't crash
    company_name = ""
    while(company_name == ""):
        company_name = input('Enter your company name: ')
        if company_name == "":
            logging.warning("Company name must not be empty!")

    address = input('Enter your company address: ')

    email = input("Enter your company email: ")

    # Create company object
    s = Company(company_name=company_name, address=address, email=email)

    # Open a session with the DB
    sesh = Session(engine)

    # Add our model instance to the session
    sesh.add(s)

    # Commit the changes and store in DB
    sesh.commit()

    # Move onto the query menu
    db_menu()


def officer_register_menu():
    '''Officer enters their information and is added to the DB'''

    print('Officer Registration ============')

    # Handle invalid inputs so the program doesn't crash
    officer_id = ""
    while(officer_id == ""):
        officer_id = input('Enter your officer ID number: ')
        if officer_id == "":
            logging.warning("Officer ID number must not be empty!")

    # Optional Inputs
    name = input("Enter your name: ")

    club_title = input('Enter the name of your club: ')

    # Create officer object
    s = Officer(officer_id=officer_id, club_title=club_title, name=name)

    # Open a session with the DB
    sesh = Session(engine)

    # Add our model instance to the session
    sesh.add(s)

    # Commit the changes and store in DB
    sesh.commit()

    # Move onto the query menu
    db_menu()


def student_register_menu():
    '''Student enters their information and is added to the DB'''

    print('Student Registration ============')

    # Handle invalid inputs so the program doesn't crash
    student_id = ""
    while (student_id == ""):
        student_id = input("Enter your student ID: ")
        if student_id == "":
            logging.warning("Student ID can not be empty!")

    name = ""
    while(name == ""):
        name = input('Enter your name: ')
        if name == "":
            logging.warning("Name must not be empty!")


    # Optional Inputs
    email = input('Enter your email address or press enter to leave it blank: ')
 
    address = input('Enter your address or press enter to leave blank: ')

    phone = input('Enter your phone number or press enter to leave blank: ')

    # Create student object
    s = Student(student_id=student_id, name=name, email=email, address=address, phone=phone)

    # Open a session with the DB
    sesh = Session(engine)

    # Add our model instance to the session
    sesh.add(s)

    # Commit the changes and store in DB
    sesh.commit()

    # Move onto the query menu
    db_menu()


def duties_entry_menu(internship_id):
    '''Student enters their duties for an internship and is added to the DB'''

    internship_id = internship_id

    print('Duties Entry ============')

    # Handle invalid inputs so the program doesn't crash
    title = input("Enter your job title at the internship or press enter to leave it blank: ")

    experience = input("Describe your experience at the internship or press enter to leave it blank: ")

    projects = input("List the projects you worked on at the internship, separated by commas: ")

    # Create student object
    s = Duties(internship_id=internship_id, title=title, experience=experience, projects=projects)

    # Open a session with the DB
    sesh = Session(engine)

    # Add our model instance to the session
    sesh.add(s)

    # Commit the changes and store in DB
    sesh.commit()

    # Move onto the query menu
    db_menu()


def reg_menu():
    '''Registration menu'''
    print("Registration ============")
    print("1. Student")
    print("2. Officer (must have student login)")
    print("3. Company")

    inputs = ["1", "2", "3"]

    user_in = None

    while user_in not in inputs:
        user_in = input('> ')
        if user_in == "1":
            student_register_menu()
        elif user_in == "2":
            officer_register_menu()
        elif user_in == "3":
            company_register_menu()


def main_menu(logged_in: bool):
    '''main menu to handle first set of inputs'''

    available_inputs = ["1", "2"]  # different way to handle invalid input

    user = None

    while user not in available_inputs:
        if logged_in == False:
            print("FGCU Student Internship DB =================")
            print("1. Register")
            print("2. Login")
            # TODO add officer login
            # TODO create company login and add internship

            user = input('> ')

            if user == "1":
                reg_menu()
            elif user == "2":
                login_menu() # Not handled yet
            else:
                logging.warning("Invalid selection!")
        else:
            db_menu()


def main():
    '''Main function that get's called on startup'''
    create_db_and_tables()
    main_menu(False)

    '''
    # idk try to get some response
    response = r.get('http://127.0.0.1:8000/3')
    print(response.json())
    '''


if __name__ == '__main__':
    main()
