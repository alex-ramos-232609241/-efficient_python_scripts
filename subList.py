def solution(listA, listB):
    # TODO: implement solution
    nb = len(listB)
    na = len(listA)
    if nb > na:
        return False
    
    new_list = []
    item = []
    for i in range(na):
        if na - i < nb:
            break
        new_list.append(listA[i:nb+i])
    
    if listB in new_list:
        return True
    return False
print(solution([1,2,3,5,6,8,9,10],[3]))