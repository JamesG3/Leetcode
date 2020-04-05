class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        cur_sum = 0
        
        for i, n in enumerate(nums):
            if cur_sum == nums_sum - cur_sum - n:
                return i
            cur_sum += n
        return -1
    
'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Solution: Traverse the list, keep calculating the prefix sum, comparing with thee rest of sum after excluding the next element as the pivot, if equal, return the pivot

Time: O(n)
Space: O(1)
'''
