def reverse_string(s):
    # TODO: implement the function to reverse the string using recursion.
    n = len(s)
    if n <= 0:
        return ''
    
    return s[n-1] + reverse_string(s[:n-1])

print(reverse_string("alex ramos"))