# question1
import time
import sys

def full_list_no_lazy():
    start_time = time.time()
    arr = list(range(0, 10001))
    end_time = time.time()
    print("Time:", end_time - start_time)
    print("Memory size:", sys.getsizeof(arr))
    print("Type:", type(arr))
    return arr

def full_list_lazy():
    start_time = time.time()
    arr_gen = (i for i in range(0, 10001))
    end_time = time.time()
    print("Time:", end_time - start_time)
    print("Memory size (generator object):", sys.getsizeof(arr_gen))
    print("Type:", type(arr_gen))
    return arr_gen

def first_5000_no_lazy(full_arr):
    start_time = time.time()
    arr_5000 = full_arr[:5000]
    end_time = time.time()
    print("Time:", end_time - start_time)
    print("Memory size:", sys.getsizeof(arr_5000))
    print("Type:", type(arr_5000))
    return arr_5000

def first_5000_lazy(full_gen):
    start_time = time.time()
    arr_5000 = list(next(full_gen) for _ in range(5000))
    end_time = time.time()
    print("Time:", end_time - start_time)
    print("Memory size:", sys.getsizeof(arr_5000))
    print("Type:", type(arr_5000))
    return arr_5000

print("No Lazy")
full_arr = full_list_no_lazy()
arr_5000_no_lazy = first_5000_no_lazy(full_arr)
print("Type match:", type(arr_5000_no_lazy) == type(full_arr))

print("Lazy")
full_gen = full_list_lazy()
arr_5000_lazy = first_5000_lazy(full_gen)
print("Type match:", type(arr_5000_lazy) == type(full_gen))

# question2
def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

gen = prime_generator()
print(next(gen))
print(next(gen))

#question3
def exp_generator(x):
    def factorial(n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

    total = 0
    n = 0
    while True:
        total += (x ** n) / factorial(n)
        yield total
        n += 1

g = exp_generator(4)
for _ in range(8):
    print(next(g))