def get_penta_num(n):
    return n * (3 * n - 1) // 2

def pentaNumRange(n1, n2):
    return [get_penta_num(i) for i in range(n1, n2 + 1)]