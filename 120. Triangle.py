class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i, row in enumerate(triangle):
            if i == 0:
                continue
                
            for j, n in enumerate(row):
                left, right = j-1, j
                if left < 0:
                    left = float('inf')
                else:
                    left = triangle[i-1][left]
                    
                if right > i-1:
                    right = float('inf')
                else:
                    right = triangle[i-1][right]
                    
                triangle[i][j] += min(left, right)
                
        return min(triangle[-1])
                    
'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example:
[[2],
[3,4],
[6,5,7],
[4,1,8,3]]
The minimum path sum from top to bottom is 11 (2 + 3 + 5 + 1 = 11).

Solution: DP
Time: O(n)
Space: extra O(1)
'''
