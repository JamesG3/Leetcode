class Solution(object):
    def minMoves2(self, nums):
        length = len(nums)
        median = sorted(nums)[length/2]
        
        result = 0
        for n in nums:
            result += abs(median-n)
            
        return result
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, 
        # where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
        # You may assume the array's length is at most 10,000.

