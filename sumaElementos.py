def sumElements(arr):
    if len(arr) == 0:
        return 0
    
    return arr[0] + sumElements(arr[1:])

print(sumElements([2, 3, 4, 5, 8]))
