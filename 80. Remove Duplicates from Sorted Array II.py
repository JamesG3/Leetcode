class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 
        
        j, counter = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                counter += 1
            
            else:
                counter = 1
                
            if counter < 3:
                nums[j] = nums[i]
                j += 1
                
        return j
                
'''
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Solution: Two pointers, inplace overwrite
Time: O(n)
Space: O(1)
'''    
                
            
                
            
            
