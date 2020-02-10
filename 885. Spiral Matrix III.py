class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = [[r0, c0]]
        for steps in range(1, 2 * (R + C), 2):
            for x, y, stp in [[0, 1, steps], [1, 0, steps], [0, -1, steps + 1], [-1, 0, steps + 1]]:
                for s in range(stp):
                    r0 += x
                    c0 += y

                    if 0 <= r0 < R and 0 <= c0 < C:
                        res.append([r0, c0])

                    if len(res) == R*C:
                        return res

'''
On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.
Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.
Now, we walk in a clockwise spiral shape to visit every position in this grid. 
Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 
Eventually, we reach all R * C spaces of the grid.
Return a list of coordinates representing the positions of the grid in the order they were visited.

Solution: Array & List, Simulation

Time: O(max(R, C) ** 2)
Space: O(R * C)
'''

