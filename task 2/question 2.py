split_lists = lambda lst: (
    list(filter(lambda x: x % 2 == 0, lst)),
    list(filter(lambda x: x % 2 != 0, lst))
)

def multiply_consecutive():
    return lambda lst: list(map(lambda i: lst[i] * lst[i + 1], range(len(lst) - 1)))

def linear_with_next(a=0.5, b=2):
    return lambda lst: list(map(lambda i: lst[i] / 2 + 2 + lst[i + 1], range(len(lst) - 1)))

sum_results = lambda lst1, lst2: (sum(lst1), sum(lst2))