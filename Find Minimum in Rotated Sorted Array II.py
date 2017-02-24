class Solution(object):
    def findMin(self, nums):
        #return min(nums)
        
        MIN = nums[0]           #worst case is O(n)
        mark = 0
        
        for n in nums:
            if n < MIN:
                return n
        return MIN
                
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
        #(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
        #Find the minimum element.
        #The array may contain duplicates.
        
