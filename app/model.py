class Person:

    def __init__(self):
        self.name = None
        self.birthday = None

class User(Person):

    def __init__(self, username, password, id = None):
        super().__init__()
        self.username = username
        self.password = password
        self.id = id
        self.activities = []

    def __repr__(self):
        return f"User({self.username})"

    def add_activity(self, activity_name, **kwargs):
        if activity_name not in self:
            self.activities.append(Activity(activity_name, **kwargs))
        else:
            print('Activity previously added.')

    def delete_activity(self, activity_name):
        if activity_name in self:
            for i, activity in enumerate(self.activities):
                if activity_name == activity.activity_name:
                    del self.activities[i]
                    print('Activity deleted.')
                    break
        else:
            print('Activity not found.')

    def edit_activity_name(self, current_activity_name, new_activity_name):
        for activity in self.activities:
            if current_activity_name == activity.activity_name:
                for activity in self.activities:
                    if new_activity_name == activity.activity_name:
                        print("An activity with the new name was previously added.")
                activity.activity_name = new_activity_name
                print("Activity name updated.")
        print("Activity not found.")

    def update_activity_metric(activity_name, metric, new_value):
        for activity in self.activities:
            if activity_name == activity.activity_name:
                activity.edit_metric(metric, new_value)

    def __contains__(self, activity_name):
        for activity in self.activities:
            if activity_name == activity.activity_name:
                return True
        return False


class Activity:

    def __init__(self, activity_name, **kwargs):
        self.activity_name = activity_name
        self._metrics = []

    def edit_metric(metric, new_value):
        for m in self.metrics:
            if metric == m.name:
                m.value = new_value


class Metric:

    def __init__(self, name, value):
        self.name = name
        self.value = value