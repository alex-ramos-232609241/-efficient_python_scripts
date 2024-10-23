def solution(grid):
    # TODO: implement the solution here
    """
    -return [min, max]
    """
    if len(grid) == 0:
        return [None, None]
    
    n = len(grid)
    
    row = n - 1
    colum = 0
    
    min = None
    max = None
    
    while row >= 0 and colum < n:
        if min is None and max is None:
            min = grid[row][colum]
            max = grid[row][colum]
        elif grid[row][colum] <= min: 
            min = grid[row][colum]
        elif grid[row][colum] >= max:
            max = grid[row][colum]
        
        colum += 1
        row -= 1
    return [min, max]