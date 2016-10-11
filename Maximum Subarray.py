class Solution(object):
    def maxSubArray(self, nums):
        
        tem=nums[0]
        ans=nums[0]
        
        for n in nums[1:]:
            if tem<0:
                tem=n
            else:
                tem+=n
            ans=max(ans,tem)
        return ans
                
                
        """
        :type nums: List[int]
        :rtype: int
        """
        
