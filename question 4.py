def is_prime(n):
    if not isinstance(n, int) or n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_twin_prime(n):
    try:
        n = int(n)
    except (ValueError, TypeError):
        return "invalid input"
    if is_prime(n) and is_prime(n + 2):
        return True
    else:
        return "invalid input"

num = input("enter number:\n")
result = is_twin_prime(num)
print(result)

def print_twin_primes(limit):
    prev = 2
    for n in range(3, limit + 1, 2):
        if is_prime(n):
            if n - prev == 2:
                print(f"({prev}, {n})")
            prev = n
