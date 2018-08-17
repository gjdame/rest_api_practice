#!/usr/bin/python3
'''people.py file to create API endpoint'''
from datetime import datetime
from flask import make_response, abort
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# data to serve people with our API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lanme": "Farrell",
        "timestamp": get_timestamp()
    },
    "Dame": {
        "fname": "Greg",
        "lname": "Dame",
        "timestamp": get_timestamp()
    },
    "Johnson": {
        "fname": "Dwayne_THE_ROCK",
        "lname": "Johnson",
        "timestampe": get_timestamp()
    }
}
#handler for GET people
def read():
    """ Function responds to request for /api/people
    returns sorted list of people"""
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def create(person):

    lname = person.get('lname', None)
    fname = person.get('fname', None)


    if lname in PEOPLE:
        abort(406, 'Person with last name {} already exists'.format(lname))
    else:
        PEOPLE[lname] = {
            'lname': lname,
            'fname': fname,
            'timestamp': get_timestamp()
        }
        return make_response('{} successfully created'.format(lname), 201)

def read_one(lname):

    #check if in people
    if lname in PEOPLE:
        person = PEOPLE.get(lname)


    else:
        abort(404, "Person with last name {} does NOT exist".format(lname))


    return (person)
