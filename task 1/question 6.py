def double(x):
    return x * 2

def square(x):
    return x ** 2

def inverse(x):
    return 1 / x if x != 0 else None

funcs = {
    "double": double,
    "square": square,
    "inverse": inverse
}
numbers = [1, 2, 4, 8]
results = {}
for name, func in funcs.items():
    results[name] = [func(n) for n in numbers]
print(results)