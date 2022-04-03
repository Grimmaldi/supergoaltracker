class Metric:
    """Metric types include: integers, strings, booleans, durations (minutes)"""

    def __init__(self, name, value):
        self.name = name
        self.value = value


class CountMetric(Metric):
    pass