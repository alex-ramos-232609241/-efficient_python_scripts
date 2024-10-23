def are_coprime(a, b):
    # TODO: implement
    while b != 0:
        print(a%b)
        a, b = b, a % b
    return a == 1

print(are_coprime(12, 18))