class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            even = (mid % 2 == 0)
            
            if even:
                if nums[mid] == nums[mid+1]:
                    left = mid + 2
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid-1]:
                    left = mid + 1
                else:
                    right = mid
                    
        return nums[right]
    
'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
Note: Your solution should run in O(log n) time and O(1) space.

Solution: Binary Search
Time: O(logn)
Space: O(1)
'''
