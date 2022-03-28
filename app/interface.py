def welcome():
    print('Welcome to SuperGoal Tracker!')

def new_user():
    username = input('Please provide a username.\n')
    activities = add_activity_form()
    return username, activities

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