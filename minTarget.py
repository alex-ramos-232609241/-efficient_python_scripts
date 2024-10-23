def count_less_than(matrix, target):
    # TODO: Your code goes here. Remember that the matrix is sorted row-wise and column-wise!
    n = len(matrix)
    m = len(matrix[0])

    count = 0
    row = n - 1 
    colum = 0

    while row >= 0 and colum < m:
        if matrix[row][colum] < target:
            count += row + 1
            colum += 1  
        else:
            row -= 1
    
    return count

matrix = [[1,2,3,4],[2,3,4,5]]
print(count_less_than())