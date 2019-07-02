class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        Solution: DP
        Time: O(n^2)
        Space: O(n^2)
        """
        if numRows == 0:
            return []
        
        res = [[1]]
        for _ in xrange(numRows-1):
            row = res[-1]
            res.append([x + y for x,y in zip([0] + row, row + [0])])
            
        return res

# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
