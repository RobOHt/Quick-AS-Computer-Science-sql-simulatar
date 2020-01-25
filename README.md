# Quick sql simulator for A-level Computer Science students
This repository holds all the nessesary code and instructions for a student
to correctly setup a real (sqlite3) database and practice sql with it.

A degree of python and command-line interface experience is assumed.

## Install requirements
There are a couple things to __install__ first.
Open the (terminal) and follow the steps

#### 1) Install (python)
open terminall and type code($ brew install python3)
If brew is not installed, install it in [brew official site]( http://brew.sh/)

#### 2) Install python packages
type in terminal code($ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py)
then type code($ python get-pip.py)
then navigate into the folder containing this repository using (cd) commands
then type code($ pip install -r requirements.txt)

## Activate virtual environment

A virtualenv is required before a database could be created

### create virtualenv: 

code(virtualenv mypython)

### Activate virtualenv: 

#### Mac OS / Linux
code($ source mypython/bin/activate)
#### Windows
code($ mypthon\Scripts\activate)

## Run the python code that automatically creates a database called (database.db)

code($ python Trainsqlite3.py)

## Enter database (database.db)

code(sqlite3 database.db)

## Now you may apply and practive your sql knowledge at well in this database!

