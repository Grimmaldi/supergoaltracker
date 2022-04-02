def new_user(users):
    keep_checking = True
    while keep_checking:
        username = input('Please provide a new username that is more than two characters in length.\n')
        for user in users:
            if username == user["username"]:
                print("Sorry, that user name is already taken.  Select again.")
                break
        keep_checking = False
        if len(username.strip()) < 2:
            print("User name must be at least two characters in length.")
            keep_checking = True
            continue
    password = input('Please select a password. \n').strip()
    id = len(users) + 1
    user_tuple = (username, password, id) 
    return user_tuple

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
            return (username, password, id)
    else:
        print("No user of this name found.  Please create a new user.")
        username, password, id = new_user(users)
        return (username, password, id)
    

    


def welcome(users):
    print('Welcome to SuperGoal Tracker!')
    while True:
        selection = input('If you are a new user, enter 1 to create a new account.  Enter 2 to sign in with an existing account.')
        if selection.strip() == '1':
            new_tuple = new_user(users)
            username = new_tuple[0]
            password = new_tuple[1]
            id = new_tuple[2]
            responses = (username, password, id)
            return responses
        elif selection.strip() == '2':
            new_tuple = existing_user(users)
            username = new_tuple[0]
            password = new_tuple[1]
            id = new_tuple[2]
            responses = (username, password, id)
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


