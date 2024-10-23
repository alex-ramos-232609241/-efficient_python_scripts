def nth_prime(n: int) -> int:
    # TODO: implement the function
    def is_prime(value):
        for i in range(2, int(value**0.5)+1):
            if value%i == 0:
                return False
        return True
    count = 1
    value = 2
    while count <= n:
        if is_prime(value):
            if count == n:
                break
            count += 1
        value += 1
      
    return value

print(nth_prime(6))
#count = 1 value = 2
#count = 2 value = 3
#count = 3 value = 5
#count = 4 value = 7