def solution(listA, listB):
    # TODO: implement solution
    nb = len(listB)
    na = len(listA)
    if nb > na:
        return False
    
    for i in range(na-nb+1):
        match = True
        for j in range(nb):
            if listA[i + j] != listB[j]:
                match = False
                break
        if match:
            return True

    return False
print(solution([1,2,3,5,6,8,9,10],[1,2,2]))