class User:

    def __init__(self, name):
        self.name = name
        self._activities = []


class Activity:

    def __init__(self, activity_name):
        self.activity_name = activity_name
        self._metrics = []