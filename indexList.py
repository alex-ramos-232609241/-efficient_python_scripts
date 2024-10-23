def solution(lst, val):
    # TODO: Implement the function
    lst_enum = list(enumerate(lst))
    def list_enumerate(data, val):
        if len(data) <= 0:
            return -1
        index, value = data[0]
        if value == val:
            return index
        else:
            return list_enumerate(data[1:], val)
        
    return list_enumerate(lst_enum, val)

print(solution([2,6,8,3,4], 6))