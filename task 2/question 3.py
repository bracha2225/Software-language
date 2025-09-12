from datetime import datetime

def date_range_closure():
    return lambda start, end: [start, (end - start).days]

def batch_date_range_closure():
    return lambda dates: list(map(lambda pair: [pair[0], (pair[1] - pair[0]).days], dates))