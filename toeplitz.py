from typing import List

def is_toeplitz(matrix: List[List[int]]) -> bool:
   # TODO: implement
    n = len(matrix)
    for i in range(1, n):
        for j in range(1, len(matrix[i])):
           
            if matrix[i][j] != matrix[i-1][j-1]:
               return False
            
    return True   
               
matrix =  [[4, 4, 4, 4], [1, 4, 4, 4], [4, 1, 4, 4], [4, 4, 0, 4]]
# 6 7 8 4  00 01 02 03
# 4 6 7 8  10 11 12 13
# 1 4 6 7  20 21 22 23
# 1 1 4 6  30 31 32 33
print(is_toeplitz(matrix))