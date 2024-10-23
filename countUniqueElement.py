def count_unique_elements(lst):
    # TODO: Implement the function that counts unique elements in the given list.
    result = []
    for i in range(len(lst)):
        new_lst = lst[:i] + lst[i+1:]
        print(new_lst)
        if lst[i] not in new_lst:
            result.append(lst[i])
    
    return len(result)

print(count_unique_elements([2,5,6,8,3,2,8]))