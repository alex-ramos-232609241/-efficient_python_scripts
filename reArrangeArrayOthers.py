def rearrange_array(arr):
    n = len(arr)
    
    quarter = n // 4
    mid_start = quarter
    mid_end = n - quarter
    
    middle_half = arr[mid_start:mid_end] 
    left_quarter = arr[:mid_start]       
    right_quarter = arr[mid_end:]        
    
    arr[:] = middle_half + left_quarter + right_quarter
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]

    
print(rearrange_array(arr))