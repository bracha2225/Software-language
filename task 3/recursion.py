# question1
def make_tuple_recursive(n):
    if n == 0:
        return ()
    return make_tuple_recursive(n-1) + (n,)

def make_tuple_tail(n, acc=()):
    if n == 0:
        return acc
    return make_tuple_tail(n-1, (n,) + acc)

t1 = make_tuple_recursive(1000)
t2 = make_tuple_tail(1000)

# question2
def sum_recursive(arr):
    if not arr:
        return 0
    return arr[0] + sum_recursive(arr[1:])

def sum_tail(arr, acc=0):
    if not arr:
        return acc
    return sum_tail(arr[1:], acc + arr[0])

print(sum_recursive(t1))
print(sum_tail(t2))

# question3
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def lcm_recursive(a, b):
    return abs(a * b) // gcd_recursive(a, b)


def gcd_tail(a, b):
    if b == 0:
        return a
    return gcd_tail(b, a % b)

def lcm_tail(a, b):
    return abs(a * b) // gcd_tail(a, b)

print(lcm_recursive(6, 4))
print(lcm_tail(6, 4))

# question4
def is_palindrome_recursive(num):
    s = str(num)

    def helper(left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return helper(left + 1, right - 1)

    return helper(0, len(s) - 1)

def is_palindrome_tail_recursive(num):
    s = str(num)

    def helper(left, right, acc=True):
        if not acc:
            return False
        if left >= right:
            return True
        return helper(left + 1, right - 1, acc and s[left] == s[right])

    return helper(0, len(s) - 1)

print(is_palindrome_recursive(123454321))
print(is_palindrome_tail_recursive(123454321))

# question5
def sortedzip_recursive(lists):
    zipped = list(zip(*lists))

    def recursive_sort(lst):
        if not lst:
            return []
        head = lst[0]
        tail_sorted = recursive_sort(lst[1:])

        def insert(x, sorted_lst):
            if not sorted_lst:
                return [x]
            if x <= sorted_lst[0]:
                return [x] + sorted_lst
            return [sorted_lst[0]] + insert(x, sorted_lst[1:])

        return insert(head, tail_sorted)

    return recursive_sort(zipped)

def sortedzip_tail(lists):
    zipped = list(zip(*lists))

    def recursive_sort_tail(lst, acc):
        if not lst:
            return acc
        head = lst[0]

        def insert_tail(x, sorted_lst):
            if not sorted_lst:
                return [x]
            if x <= sorted_lst[0]:
                return [x] + sorted_lst
            return [sorted_lst[0]] + insert_tail(x, sorted_lst[1:])

        return recursive_sort_tail(lst[1:], insert_tail(head, acc))

    return recursive_sort_tail(zipped, [])

lists = [[3,1,2],[5,6,4],['a','b','c']]
print(sortedzip_recursive(lists))
print(sortedzip_tail(lists))
