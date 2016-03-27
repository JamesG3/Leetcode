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
