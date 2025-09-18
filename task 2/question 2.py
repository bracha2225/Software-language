linear = lambda x: x/2 + 2
numbers = list(range(1, 1001))

split_lists = lambda lst: (
    list(filter(lambda x: x % 2 == 0, lst)),
    list(filter(lambda x: x % 2 != 0, lst))
)

evens, odds = split_lists(numbers)

multiply_consecutive = lambda lst: [lst[i] * lst[i + 1] for i in range(len(lst) - 1)]
linear_with_next = lambda lst: [linear(lst[i]) + lst[i + 1] for i in range(len(lst) - 1)]

evens_multiplied = multiply_consecutive(evens)
odds_multiplied = multiply_consecutive(odds)

evens_linear = linear_with_next(evens)
odds_linear = linear_with_next(odds)

sum_evens_multiplied = sum(evens_multiplied)
sum_odds_multiplied = sum(odds_multiplied)

sum_evens_linear = sum(evens_linear)
sum_odds_linear = sum(odds_linear)
