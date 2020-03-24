class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        
        if 1 not in nums:
            return 1
        if nums == [1]:
            return 2
        
        for i, n in enumerate(nums):
            if n <= 0 or n > length:
                nums[i] = 1
                
        for i, n in enumerate(nums):
            absn = abs(n)
            if absn == length:
                nums[0] = - abs(nums[0])
            else:
                nums[absn] = - abs(nums[absn])
                   
        for i in range(1, length):
            if nums[i] > 0:
                return i
            
        if nums[0] > 0:
            return length
        
        return length + 1
                
'''
Given an unsorted integer array, find the smallest missing positive integer.
Solution: Index, trick, list, traverse and mark, edge case
    - pre-process the list to remove invalid elements
    - use index to mark the positive number, flip the sign for each existing pos number
    - use the first element index-0 to store the number index-len(nums)
Time: O(n)
Space: O(1)
'''
