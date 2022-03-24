import interface
from model import User, Activity


class Session:

    # TODO: Create Database/ connection

    def __init__(self) -> None:
        interface.welcome()
        username = input('What is your username?')
        if username not in db:
            user = User(username)
        else:
            # TODO: load user from DB 
            NotImplemented

    
