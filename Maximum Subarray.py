class Solution(object):
    def maxSubArray(self, nums):
        
        tem=nums[0]                 #initialize the tem sum as the first number in nums
        ans=nums[0]                 #initialize the final sum as the first number in nums
        
        for n in nums[1:]:          #read from the second number
            if tem<0:               #if the tem is negative, then whatever the next number is, update tem sum with the value of n
                tem=n
            else:                   #if the tem is positive, then add tem with n
                tem+=n
            ans=max(ans,tem)        #compare the ans and tem, always save the larger one
        return ans
                
                
        """
        :type nums: List[int]
        :rtype: int
        
        Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
        For example, given the array [-2,1,-3,4,-1,2,1,-5,4]
        The contiguous subarray [4,-1,2,1] has the largest sum = 6.
        """
        
