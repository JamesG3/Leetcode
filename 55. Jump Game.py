class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Solution: Greedy, calculate the max length can be reached, traverse all elements in nums, return False when current element cannot be reached
        Time: O(n)
        Space:O(1)
        """
        max_len_reach = nums[0]
        length = len(nums)
        
        for i in xrange(1, length):
            if max_len_reach < i:
                return False
            
            max_len_reach = max(max_len_reach, nums[i] + i)
            
        return True
        
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.


