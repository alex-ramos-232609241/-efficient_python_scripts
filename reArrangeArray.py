def rearrange_array(nums):
    # TODO: implement the function.
    n = len(nums)
    k = n//4
    p = n%4
    add1 = 0
    add2 = 0
    if p == 2 or p == 1:
        add1 = 1
        add2 = p - add1
    elif p == 3:
        add1 = 2
        add2 = p - add1
    
        
    return nums[k:2*k+add1] + nums[2*k+add1:3*k+add1 + add2] + nums[:k] + nums[3*k+add1+add2:]
print(rearrange_array([1, 1, 1, 1, 2, 3, 4, 5]))
[1, 1, 2, 3, 1, 1, 4, 5]