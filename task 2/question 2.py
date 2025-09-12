numbers = list(range(1, 1001))

split_lists = lambda lst: (
    list(filter(lambda x: x % 2 == 0, lst)),
    list(filter(lambda x: x % 2 != 0, lst))
)
even_list, odd_list = split_lists(numbers)

def multiply_consecutive():
    return lambda lst: list(map(lambda i: lst[i] * lst[i + 1], range(len(lst) - 1)))

def linear_with_next(a=0.5, b=2):
    return lambda lst: list(map(lambda i: lst[i] / 2 + 2 + lst[i + 1], range(len(lst) - 1)))

even_multiplied = multiply_consecutive()(even_list)
odd_linear_next = linear_with_next()(odd_list)

sum_results = lambda lst1, lst2: (sum(lst1), sum(lst2))
sum_even, sum_odd = sum_results(even_multiplied, odd_linear_next)

print(f"Sum of multiplied consecutive elements in even list: {sum_even:.2f}")
print(f"Sum of linear function with next element in odd list: {sum_odd:.2f}")