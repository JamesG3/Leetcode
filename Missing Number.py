class Solution(object):
    def missingNumber(self, nums):
        ans=(max(nums)+min(nums))*(len(nums)+1)/2-sum(nums)
        if(ans in nums):
            if(0 in nums):
                return max(nums)+1
            else:
                return 0
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        #Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array. 
