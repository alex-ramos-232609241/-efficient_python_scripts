def get_prime_factors(n):
    # TODO: Implement the function that returns all prime factors of n
    result = []
    def is_prime(v):
        for i in range(2, int(v**0.5)+1):
            if v%i == 0:
                return False
        return True
        
    value = 2
    while value < n+1:
        if n%value == 0 and is_prime(value):
            print(value)
            result.append(value)
        value = value + 1   
    return result    

print(get_prime_factors(27))