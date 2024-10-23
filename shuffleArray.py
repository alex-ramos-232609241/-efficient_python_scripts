def shuffle_array(nums, k):
    n = len(nums)  
    i = 0
    real_index = k - 1  
    m = 0
    while i < n and real_index < n:
        k_index = real_index - m
        print("k_index")
        print(k_index)
        print("***k_index")
        value = nums[k_index]

        for j in range(k_index + 1, n):
            nums[j - 1] = nums[j]
        m += 1
        nums[n - 1] = value
        real_index = real_index + k
        i += 1

    return nums

nums = [199, 299, 399, 499, 599, 699, 799]
[199, 299, 499, 599, 799, 399, 699]
k = 3
result = shuffle_array(nums, k)
print(result)