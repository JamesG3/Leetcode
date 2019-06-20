class Solution(object):
    def __init__(self):
        self.res = [[]]
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Solution: DFS, use tmp_list to represent each tree node when traversing the entire tree
        Time: O(n^2)
        Space: O(n^2)
        
        """
        
        nums.sort()
        self.helper(nums, [])
        return self.res
        
        
    def helper(self, nums, tmp_list):
        if not nums:
            return
        
        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == n:
                continue
            
            t = tmp_list + [n]
            self.res += [t]
            self.helper(nums[i+1:], t)
      
        
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.    
        
