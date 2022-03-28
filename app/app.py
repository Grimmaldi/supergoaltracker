from app.interface import welcome
from app.model import User, Activity
import json


class Session:

    def __init__(self):
        
        with open('./app/db.json') as dbfile:
            db = json.load(dbfile)

        welcome()
        username = input('What is your username?')
        password = input('What is your password.')
        if username not in db:
            user = User(username, password)
        else:
            # TODO: load user from DB 
            NotImplemented

    
