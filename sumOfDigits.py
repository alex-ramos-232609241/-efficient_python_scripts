def sum_of_digits(value):
    if value == 0:
        return 0
    
    return value%10 + sum_of_digits(value//10)

print(sum_of_digits(152))