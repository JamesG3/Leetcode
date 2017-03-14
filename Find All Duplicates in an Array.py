class Solution(object):
    def findDuplicates(self, nums):
        res = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                res.append(abs(n))
            nums[abs(n)-1] = -nums[abs(n)-1]
                
        return res
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # time: O(n), space:O(1)
        
        # because 1 ≤ a[i] ≤ n (n = size of array)
        # n can be used as index for this array
        # set the corresponding number to negative, when a number is set twice, the index must appear twice!
