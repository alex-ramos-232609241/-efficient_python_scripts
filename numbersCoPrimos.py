def are_coprime(a, b):
    # TODO: implement
    n = 2
    result = []
    if a > b:
        val = b
    else:
        val = a
  
    while n < val:
        if a%n == 0 and b%n == 0:
            result.append(n)
        n += 1
    if len(result) > 0:
        return False
    else:
        return True        

print(are_coprime(12, 18))