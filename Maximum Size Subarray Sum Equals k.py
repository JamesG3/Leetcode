class Solution:
    def maxSubArrayLen(self, nums, k):
        
        res = 0
        currsum = 0     # calculate accumulated sum from left to right
        dic = {0:0}     # use dictionary to store each possible currsum and the first time it appears, O(1) to look up
        
        for i in range(len(nums)):
            currsum += nums[i]
            if currsum not in dic:
                dic[currsum] = i+1
            if currsum-k in dic:
                res = max(res,  i+1-dic[currsum-k])
        return res
        
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        # Given an array nums and a target value k, find the maximum length of a subarray that sums to k. 
        # If there isn't one, return 0 instead.
