def new_user(users):
    keep_checking = True
    while keep_checking:
        username = input('Please provide a new username that is more than two characters in length.\n')
        for user in users:
            if username == user["username"]:
                print("Sorry, that user name is already taken.  Select again.")
                username = ''
                break
            elif len(username.strip()) < 2:
                print("User name must be at least two characters in length.")
                username = ''
                break
            else:
                keep_checking = False
    password = input('Please select a password. \n').strip()
    id = len(users) + 1
    return {"username": username, "password": password, "id": id, "is_new": True}

def existing_user(users):
    username = input('Please enter you username: ')
    for user in users:
        if username == user["username"]:
            print("Username found.")
            id = user["id"]
            stored_password = user["password"]
            password = input('Please enter your password: ')
            if password != stored_password:
                raise ValueError("Incorrect password")
            return {"username": username, "password": password, "id": id, "is_new": False}
    else:
        print("No user of this name found.  Please create a new user.")
        username, password, id = new_user(users)
        return {"username": username, "password": password, "id": id, "is_new": True}


def welcome(users):
    print('Welcome to SuperGoal Tracker!')
    while True:
        selection = input('If you are a new user, enter 1 to create a new account.  Enter 2 to sign in with an existing account.')
        if selection.strip() == '1':
            responses = new_user(users)
            return responses
        elif selection.strip() == '2':
            responses = existing_user(users)
            return responses
        else:
            print("Response not understood.")


def add_activity_form():
    activities = []
    while True:
        response = input('Do you have an activity that you would like to add? [Yes/No]').lower().trim()
        if response == 'no':
            break
        elif response == 'yes':
            activity_name = 'What is the name of the that you wish to track?'
            activities.append(activity_name)
        else:
            print('Sorry, I do not understand.  Please respond either "yes" or "no".\n')


