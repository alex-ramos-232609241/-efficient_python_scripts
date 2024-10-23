def shift_list_elements(ls, shift):
    # TODO: Implement the solution
    n = len(ls)
    result = []
    if shift%n == 0:
        return ls
    else:
        delta = shift%n
        result = ls[-delta:] + ls[:-delta]
    return result
print(shift_list_elements([2,5,6,8,3,1], 2))