from typing import List, Optional
def find_row_with_target(matrix: List[List[int]], target: int) -> Optional[int]:
    # TODO: Implement the solution here
    
    n = len(matrix)
    m = len(matrix[0])
    
    row = n - 1
    colum = 0
    result = None
    while row >= 0 and  colum < m:
        if matrix[row][colum] > target:
            row -= 1
        elif matrix[row][colum] < target:
            colum += 1
        elif matrix[row][colum] == target:
            result = row
            break
        
    return result

print(find_row_with_target([
            [-5, -3, 0, 3],
            [-2, 2, 7, 10]
        ], 12))