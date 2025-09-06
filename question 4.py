def is_prime(n):
    if not isinstance(n, int) or n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def twin_prime(n):
    if is_prime(n + 2):
        return n + 2
    elif is_prime(n - 2):
        return n - 2
    else:
        return None

def main():
    num = input("enter prime number:\n")
    try:
        n = int(num)
    except (ValueError, TypeError):
        print("invalid input")
        return

    if not is_prime(n):
        print("invalid input")
        return

    twin = twin_prime(n)
    if twin:
        print(twin)
    else:
        print("invalid input")

if __name__ == "__main__":
    main()