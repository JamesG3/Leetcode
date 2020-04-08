class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0] + k
        
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff == 1:
                continue
            
            if diff > k:
                return nums[i-1] + k
            else:
                k -= diff-1
                
        return nums[-1] + k

    
'''
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

Solutin: Math, traverse and mark, one pass
Time: O(n)
Space: O(1)
'''
