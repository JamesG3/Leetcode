class Solution(object):
    def majorityElement(self, nums):
        res=[]
        for i in set(nums):
            if(nums.count(i)>len(nums)/3):
                res.append(i)
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
        
