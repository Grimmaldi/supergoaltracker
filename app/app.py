from readline import append_history_file
from app.interface import welcome
from app.models.users import User
import json


class Session:

    def __init__(self):

        with open('./app/data/users_table.json') as users_table:
            self.users = json.load(users_table)

            self.results = self.establish_user(self.users['users'])
            self.user = self.results[0]
            self.is_new = self.results[1]
            if self.is_new == True:
                self.append_user(self.user)
            print(self.user)

    def establish_user(self, users):
        user_info = welcome(users)
        user = User(user_info["username"], user_info["password"], user_info["id"])
        return (user, user_info["is_new"])

    def append_user(user, filename='./app/data/users_table.json'):
        user_dict = {"id":user.id, "username":user.username, "password":user.password}
        with open(filename,'r+') as file:
            file_data = json.load(file)
            file_data["users"].append(user_dict)
            file.seek(0)
            json.dump(file_data, file, indent = 4)