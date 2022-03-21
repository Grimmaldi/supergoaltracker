import imp
from model import User

class Session:

    # TODO: Create Database/ connection

    def __init__(self, username) -> None:
        if username not in db:
            user = User(username)
        else:
            # TODO: load user from DB 
            NotImplemented



