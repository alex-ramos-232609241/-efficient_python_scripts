def solution(nums):
    # TODO: implement the function to return a tuple (even_count, odd_count)
    (even_count, odd_count) = (0, 0)
    
    for data_nums in nums:
    
        if data_nums%2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
        
    return (even_count, odd_count)

print(solution(list(range(-1000, 1001))))