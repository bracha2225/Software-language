linear = lambda x: x/2 + 2

lst = list(map(linear, range(0, 10001)))

sum_lst = sum(lst)

import time
start = time.time()
imperative_sum = 0
for x in lst:
    imperative_sum += x
imperative_time = time.time() - start

start = time.time()
functional_sum = sum(lst)
functional_time = time.time() - start

single_value = linear(7)