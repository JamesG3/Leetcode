class Solution(object):
    def maxKilledEnemies(self, grid):
        if grid == []:
            return 0
        rowlen, collen = len(grid[0]), len(grid)
        grid1 = []
        grid2 = []
        res = 0
        
        for row in grid:        # deal with all rows
            row1 = row
            stack = []
            Enum = 0
            for j, r in enumerate(row1):
                if r == "W":                # if wall, update previous positions in the stack
                    while stack:
                        s = stack.pop()
                        row1[s] = str(Enum)
                    Enum = 0
                elif r == "E":  
                    Enum += 1
                else:
                    stack.append(j)            # store all empty positions between two walls in stack
            while stack:                    # if there is no 'W' in the last part of list, update the remain positions
                s = stack.pop()
                row1[s] = str(Enum)
            grid1.append(row1)
        
        
        for j in xrange(rowlen):        # deal with all columns
            col = []
            stack = []
            Enum = 0
            for k in xrange(collen):
                col.append(grid[k][j])
                
            for n, c in enumerate(col):
                if c == 'W':                # if wall, update previous positions in the stack
                    while stack:
                        s = stack.pop()
                        col[s] = str(Enum)
                    Enum = 0
                elif c == 'E':
                    Enum += 1
                else:                   # store all empty positions between two walls in stack
                    stack.append(n)    
            while stack:                # if there is no 'W' in the last part of list, update the remain positions
                s = stack.pop()
                col[s] = str(Enum)
            grid2.append(col)
            
            
        for i in xrange(collen):
            for j in xrange(rowlen):
                if grid1[i][j] not in ('W','E') and grid2[j][i] not in ('W','E'):
                    res = max(res, int(grid1[i][j])+int(grid2[j][i]))
                    
        return res
        
                    
        
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        # Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
        # The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
        # Note that you can only put the bomb at an empty cell.
