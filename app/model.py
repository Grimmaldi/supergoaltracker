class User:

    def __init__(self, name):
        self.name = name
        self.activities = []

    def __repr__(self) -> str:
        return f"User({self.name})"

    def add_activity(self, activity_name, **kwargs):
        self.activities.append(Activity(activity_name, **kwargs))

    def delete_activity(self, activity_name):
        for i, activity in enumerate(self.activities):
            if activity.activity_name == activity_name:
                del self.activities[i]
                break



class Activity:

    def __init__(self, activity_name, **kwargs):
        self.activity_name = activity_name
        self._metrics = []