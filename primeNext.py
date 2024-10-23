def next_prime(n):
    # TODO: implement the function to find the next prime number after n
    prime = n + 1
    while True:
        is_prime = True
        for i in range(2, int(prime ** 0.5) + 1):
            if prime % i == 0:
                is_prime = False
                break
        if is_prime:
            return prime
        prime += 1
print(next_prime(999983))