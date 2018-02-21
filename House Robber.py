class Solution(object):
    def rob(self, nums):
        current = 0
        last = 0
        
        for n in nums:
            last, current = current, max(last+n, current)
            
        return current
        
    # dp solution
    def rob(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        
        if length < 3:
            return max(nums)
        
        if length == 3:
            return max(nums[1], nums[0]+nums[-1])
    
        dp = nums[:2] + [nums[0]+nums[2]]
        
        for i in xrange(3, length):
            dp.append(max(nums[i] + dp[-2], nums[i] + dp[-3]))
        
        return max(dp[-2:])
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #You are a professional robber planning to rob houses along a street. 
        #Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
        #Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.        
