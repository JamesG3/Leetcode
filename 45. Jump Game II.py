class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Solution: Greedy
        Time: O(n)
        Space: O(1)
        """
        length = len(nums) - 1
        max_reach = 0
        jumps = 0
        right_most = 0
        
        for i,n in enumerate(nums[:-1]):
            max_reach = max(max_reach, n + i)
            if max_reach >= length:
                return jumps + 1
            
            # when i == right_most, there must be another jump required to reach further
            # so jump to the current farmost index
            if i == right_most:
                right_most = max_reach
                jumps += 1
            
        
        return 0
            
       
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.


