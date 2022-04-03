class Activity:

    def __init__(self, activity_name, **kwargs):
        self.activity_name = activity_name
        self._metrics = []

    def edit_metric(metric, new_value):
        for m in self.metrics:
            if metric == m.name:
                m.value = new_value
