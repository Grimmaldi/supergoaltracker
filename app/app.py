from app.interface import welcome
from app.model import User, Activity
import json


class Session:

    def __init__(self):

        with open('./app/data/users_table.json') as users_table:
            users = json.load(users_table)

        user = self.establish_user(users['users'])
        print(user)
        
    def establish_user(self, users):
        user_params = welcome(users)
        username = user_params[0]
        password = user_params[1]
        id = user_params[2]
        user = User(username, password, id)
        return user
