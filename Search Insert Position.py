class Solution(object):
    def searchInsert(self, nums, target):
        p = 0
        length = len(nums)
        
        if length == 0 or target <= nums[0]:
            return 0
        
        if target > nums[-1]:
            return length

        while not (nums[p] <= target <= nums[p+1]):
            p+=1
            
        return p+1
            
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        # Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
        # You may assume no duplicates in the array.
