class Solution(object):
    def checkPossibility(self, nums):
        pointer = None
        
        for i, n in enumerate(nums[:-1]):
            if n > nums[i+1]:
                if pointer is not None:
                    return False
                pointer = i
        return (pointer is None or 
                pointer == 0 or 
                pointer == len(nums)-2 or 
                nums[pointer-1] <= nums[pointer+1] or 
                nums[pointer] <= nums[pointer+2])
            
                
                
                
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        # Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
        # We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
        
