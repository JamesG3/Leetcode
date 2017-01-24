class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        res = 0
        tem = 0
        
        for n in nums:
            if n==1:
                tem+=1
            if n==0:
                res = max(res, tem)
                tem=0
                
        return max(res,tem)
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Given a binary array, find the maximum number of consecutive 1s in this array.
        #Example 1:
        # Input: [1,1,0,1,1,1]
        # Output: 3
