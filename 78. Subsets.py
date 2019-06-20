class Solution(object):
    def __init__(self):
        self.res = [[]]
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Solution: Recursive DFS/Backtracking
        Time: O(n^2)
        Space: O(n^2)
        """
        if not nums:
            return
        
        self.subsets(nums[1:])
        tmp_res = [r + [nums[0]] for r in self.res]
        self.res += tmp_res
        
        return self.res
        

# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
       
