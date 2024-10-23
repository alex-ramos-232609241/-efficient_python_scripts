def solution(n, pos = 1):
    # TODO: implement
    if n < 1 :
        return n
    m = n % 10
    
    return m**pos + solution(n//10, pos+1)

print(solution(235))