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

if __name__ == "__main__":
    closure_func = linear_closure()
    create_list = higher_order_create_list(closure_func)
    sum_func = higher_order_sum()
    start, end = 0, 100_000

    t0 = time.time()
    y_list = create_list(start, end)
    t_create = time.time() - t0

    t0 = time.time()
    s = sum_func(y_list)
    t_sum_func = time.time() - t0

    print(f"List creation time: {t_create:.5f} seconds")
    print(f"Functional sum time: {t_sum_func:.5f} seconds, sum: {s:.2f}")

    test_x = 42
    print(f"Function value for x={test_x}: {closure_func(test_x)}")