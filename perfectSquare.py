def is_perfect_square(n):
    if n < 0:
        return False
    x = n // 2 
    dict = set()  
    
    while x * x != n:
        dict.add(x)
        x = (x + n // x) // 2  
        if x in dict: 
            return False
    return True
print(is_perfect_square(10000))