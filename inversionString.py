def inversion_string(value_str):
    if len(value_str) == 0:
      return value_str
    
    return inversion_string(value_str[1:]) + value_str[0]
    

print(inversion_string("hoy"))
