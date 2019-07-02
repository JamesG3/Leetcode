class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        Solution: iterative update the current row
        Time: O(n^2)
        Space: O(n)
        """
        row = [1]
        for _ in xrange(rowIndex):
            row = [x + y for x,y in zip([0] + row, row + [0])]
            
        return row
        
        
#Given an index k, return the kth row of the Pascal's triangle.
#For example, given k = 3,
#Return [1,3,3,1].
