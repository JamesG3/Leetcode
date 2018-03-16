class Solution(object):
    # optimized version - delete overlapped edges
    def islandPerimeter(self, grid):
        m, n = len(grid), len(grid[0])
        perimeter = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += 4
                    
                    if i<m-1 and grid[i+1][j] == 1:
                        perimeter -= 2
                    if j<n-1 and grid[i][j+1] == 1:
                        perimeter -= 2
        return perimeter
                        
    
    # brute force
    def islandPerimeter(self, grid):
        x=0
        y=0
        res=0
        if len(grid)==0:
            return res
        
        while y!=len(grid):             #traverse all points one by one
            x=0
            while x!=len(grid[0]):
                if grid[y][x]==1:       #if current number is 1
                    if y==0:                #check if the current location is on the edge(edge+1)
                        res+=1
                    if x==0:
                        res+=1
                    if y==len(grid)-1:      
                        res+=1
                    if x==len(grid[0])-1:
                        res+=1
                    if x-1 >= 0:            #check if left and right exist 0 (edge+1)
                        if grid[y][x-1]==0:
                            res+=1
                    if x+1 < len(grid[0]):
                        if grid[y][x+1]==0:
                            res+=1
                    if y-1 >= 0:            #check if up and down exist 0 (edge+1)
                        if grid[y-1][x]==0:
                            res+=1
                    if y+1 < len(grid):
                        if grid[y+1][x]==0:
                            res+=1
                x+=1
            y+=1
            
        return res
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        #give a grid which is rectangular, width and height don't exceed 100.
        #0 represents water, 1 represents island.
        #Determine the perimeter(edge) of the island.
        #example:[[0,1,0,0],
        #        [1,1,1,0],
        #        [0,1,0,0],
        #        [1,1,0,0]]
        #Has perimeter 16.
