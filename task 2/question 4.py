def power_function(exponent):
    return lambda base: base ** exponent

def power_map(n):
    return map(lambda i: lambda x: x ** i, range(1, n+1))

def powers_tuple(n, base):
    return tuple(map(lambda i: base ** i, range(n)))

n = int(input())
result = map(lambda i: lambda x: x ** i, range(n))
print(type(result))
base = int(input())
powers = tuple(map(lambda i: base ** i, range(n)))
print(powers)

def approx_exp(x, max_power):
    def factorial(n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
    total = 0
    for n in range(max_power+1):
        total += (x ** n) / factorial(n)
    return total

x = float(input())
max_power = int(input())
print(approx_exp(x, max_power))