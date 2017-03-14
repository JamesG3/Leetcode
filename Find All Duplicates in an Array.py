class Solution(object):
    def findDuplicates(self, nums):
        res = []
        
        nums.sort()
        
        for i in xrange(len(nums)-1):
            if nums[i+1] == nums[i]:
                res.append(nums[i])
        return res
        
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # time: O(n+lgn), space:O(1)
