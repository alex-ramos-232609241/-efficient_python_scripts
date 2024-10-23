from typing import List, Optional

def second_max(nums: List[int]) -> Optional[int]:
    # TODO: Find the second largest number in nums
    nums_filter = []

    for x in nums:
        if x not in nums_filter:
            nums_filter.append(x)

    n = len(nums_filter)
    if n < 2:
        return None
    
    for i in range(n):
        for j in range(0, n-i-1):
            if nums_filter[j] > nums_filter[j+1] and nums_filter[j] != nums_filter[j+1]:
                [nums_filter[j],nums_filter[j+1]] = [nums_filter[j+1],nums_filter[j]]
    
    return nums_filter[n-2] 

print(second_max([10, 10, 10, 10, 9])) 