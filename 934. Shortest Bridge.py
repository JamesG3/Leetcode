class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        for i, row in enumerate(A):
            for j, n in enumerate(row):
                if n == 1:
                    dfs = [[i, j]]
                    break
        
        # get all island1
        island1 = set([(dfs[0][0], dfs[0][1])])
        height = len(A)
        width = len(A[0])
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        while dfs:
            tmp_dfs = []
            for i, j in dfs:
                for dir_x, dir_y in dirs:
                    m, n = i + dir_x, j + dir_y
                    if (0 <= m < height) and (0 <= n < width) and (m, n) not in island1:
                        if A[m][n] == 1:
                            tmp_dfs.append([m, n])
                            island1.add((m, n))
            dfs = tmp_dfs
        
        # expand island1
        dist = 0
        dfs = [[_[0], _[1]] for _ in island1]
        while dfs:
            tmp_dfs = []
            for i, j in dfs:
                for dir_x, dir_y in dirs:
                    m, n = i + dir_x, j + dir_y
                    if (0 <= m < height) and (0 <= n < width) and (m, n) not in island1:
                        if A[m][n] == 1:
                            return dist
                        
                        else:
                            A[m][n] = 1
                            island1.add((m, n))
                            tmp_dfs.append([m, n])
            dfs = tmp_dfs
            dist += 1
                            
                            
'''
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)
Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Solution: BFS
    1. use bfs to find all area belong to island1
    2. use bfs to expand island1
    3. break if island2 found
Time, Space: O(n)
'''          
                   
