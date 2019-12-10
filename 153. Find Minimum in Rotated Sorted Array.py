class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        length = len(nums)
        if nums[0] < nums[-1]:
            return nums[0]
        
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
                
        return nums[l]
                
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.

Solution: Binary Search, if mid > right, then move right, else move left, until l == r
Time: O(log(n))
Space: O(1)
'''
