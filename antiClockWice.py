from typing import List

def anti_rotate_array(nums: List[int], k: int) -> None:
    # TODO: Implement anti-clockwise rotation of the array nums by k steps.
    n = len(nums)
    k = k % n  
    invert(nums, 0, k - 1)
    invert(nums, k, n - 1)
    invert(nums, 0, n - 1)

def invert(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

