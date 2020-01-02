class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visted = set()
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        if not grid:
            return 0
        
        height = len(grid)
        width = len(grid[0])
        
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == 0 or (i, j) in visted:
                    continue
                
                visted.add((i, j))
                stack = [[i, j]]
                area = 1
                while stack:
                    cur = stack.pop()
                    
                    for x, y in dirs:
                        m, n = cur[0]+x, cur[1]+y
                        if not (0 <= m < height and 0 <= n < width):
                            continue
                        if (m, n) in visted:
                            continue
                            
                        if grid[m][n] == 1:
                            visted.add((m, n))
                            area += 1
                            stack.append([m, n])
                            
                max_area = max(max_area, area)
        return max_area
                    
'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Solution: DFS, Hashset
Time, Space: O(n)
'''        
            
        
        
