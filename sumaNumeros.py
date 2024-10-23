def sum_primary_n(n):
    if n == 0:
        return 0
    return n + sum_primary_n(n-1)

print(sum_primary_n(5))