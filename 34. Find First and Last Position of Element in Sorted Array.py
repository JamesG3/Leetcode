class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        
        i_left = self.binarySearch('left')
        # there are two situations may match the first condition:
        #   1. nums is empty: then the returned low will be 0
        #   2. all numbers in nums are smaller than target, then low will be the length of nums
        if i_left == len(self.nums) or self.nums[i_left] != self.target:
            return [-1, -1]
        
        return [i_left, self.binarySearch('right') - 1]
        
    
    
    def binarySearch(self, flag):
        low, high = 0, len(self.nums)
        while low < high:
            mid = (low + high) // 2
            if self.nums[mid] > self.target or (flag == 'left' and self.nums[mid] == self.target):
                high = mid
            else:
                low = mid + 1
                
        return low
    
    
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].

# solution: binary search (twice)
# time: O(logn)
# space: O(1)
