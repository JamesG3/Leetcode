class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            i = abs(n) - 1
            if nums[i] < 0:
                res.append(abs(n))
            else:
                nums[i] *= -1        
        return res
    
'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Solution: Using index of a list
Time: O(n)
Space: O(1)
'''
        
