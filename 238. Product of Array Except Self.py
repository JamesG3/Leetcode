class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in nums]
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        right = 1
        for i in range(len(nums)-2, -1, -1):
            right *= nums[i+1]
            res[i] *= right
        
        return res
            
'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


Solution: Traverse and mark, math
    For example: [1,2,3,4] 
        1. get all product before each element -> [1, 1, 2, 6]
        2. traverse from the end, get all product after each element, multiply the current res: [24, 12, 6, 1]
Time: O(n), two pass
Space: extra O(1)
'''
