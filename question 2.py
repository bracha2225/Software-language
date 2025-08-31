def sum_digits(num):
    try:
        s = str(int(num))
        return sum(int(digit) for digit in s)
    except (ValueError, TypeError):
        return "invalid input"


num2 = input("Enter a number: ")
print(sum_digits(num2))