'''
 api.py - FGCU Data Engineering Internship DB Project
 API file that houses all code and logic for our 
 CRUD group final project for COP 3710. 

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

from fastapi import FastAPI
import sqlite3 as sql


# FastAPI object
app = FastAPI()

con = sql.connect("intern.db")


# root function
@app.get('/')
def root():
    return({"text": "Hello world"})


def create():
    pass


def read():
    pass


def update():
    pass


def delete():
    pass
