class Person:

    def __init__(self):
        self.name = None
        self.birthday = None

class User(Person):

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.id = None
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
                    break
        else:
            print('Activity not found.')

    def edit_activity(self, activity_name, metric, new_value):
        for i, activity in enumerate(self.aectivities):
            if activity_name == activity.activity_name:
                activity[i].edit(metric, new_value)

    def __contains__(self, activity_name):
        for activity in self.activities:
            if activity_name == activity.activity_name:
                return True
        return False

class Activity:

    def __init__(self, activity_name, **kwargs):
        self.activity_name = activity_name
        self._metrics = []


class Metric:

    def __init__(self) -> None:
        pass