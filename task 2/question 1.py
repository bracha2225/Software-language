import time

def linear_closure(a=0.5, b=2):
    return lambda x: a * x + b

def higher_order_create_list(f):
    return lambda start, end: list(map(f, range(start, end + 1)))

def higher_order_sum():
    return lambda lst: sum(lst)

def measure_time(f):
    return lambda *args, **kwargs: (
        lambda start, end: (result := f(start, end), elapsed := time.time() - (t := time.time()), result, elapsed)
    )(*args, **kwargs)[2:]