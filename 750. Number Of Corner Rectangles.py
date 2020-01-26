from collections import defaultdict
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        pairs = defaultdict(int)
        res = 0
        
        length = len(grid[0])
        for row in grid:
            for i, n in enumerate(row):
                if n != 1:
                    continue
                    
                for j in range(i+1, length):
                    if row[j]:
                        res += pairs[(i, j)]
                        pairs[(i, j)] += 1
                    
        return res
                    
                        
                    
                    
'''
Given a grid where each entry is only 0 or 1, find the number of corner rectangles.
A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.

Solution: Hashtable, Math, Combinations of C(a, b) is (a!) / (b! * (a-b)!)
Time: O(n^2 * m)
Space: O(n^2)
'''
        
