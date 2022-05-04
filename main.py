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

import requests as r
import logging


def student_registration_menu():
    print('Student Registration ============')
    print('')


def main_menu(logged_in: bool):
    if logged_in == False:
        print("FGCU Student Internship DB =================")
        print("1. Student registration")
        print("2. Student login (not real)")
    else:
        pass


def main():
    pass

    '''
    # idk try to get some response
    response = r.get('http://127.0.0.1:8000/3')
    print(response.json())
    '''


if __name__ == '__main__':
    main()
