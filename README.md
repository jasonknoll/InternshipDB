# InternshipDB
Database application for Professor Allen's Intro to Data Engineering final group project

## Installation
---
_Python 3.9.12 was used for this project_

To install all the required Python packages: 
`pip install -r reqs.txt`

In one console window run:
`python -m uvicorn api:app -reload`

And in another open the interface with:
`python main.py`


## How to use
---
This application is composed of two different systems: the text interface and the API which connects to the database and acts as a 'server' even though they're both running locally on your machine. 

This program uses **FastAPI** to handle the API requests and return JSON objects. These JSON objects translate direction into Python dictionaries and can be manipulated easily. 
