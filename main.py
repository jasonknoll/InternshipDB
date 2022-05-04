'''
 main.py - FGCU Data Engineering Internship DB Project
 Main file that houses all code and logic for our 
 group final project for COP 3710. 

 Jason Knoll, Jordan Tatum, Chance Mullen

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
