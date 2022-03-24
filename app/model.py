class User:

    def __init__(self, name):
        self.name = name
        self.activities = []

    def __repr__(self) -> str:
        return f"User({self.name})"

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
        for i, activity in enumerate(self.activities):
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