class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        length = len(nums)
        if length == 1:
            return 1 if nums[0] >= s else 0
        
        # to handle the edge case that the first element is larger than s
        if length > 1 and nums[0] >= s:
            return 1
        
        # two pointers
        i1, i2 = 0, 1
        min_len = float('inf')
        cur_sum = nums[i1] + nums[i2]
        while i1 <= i2:
            if cur_sum >= s:
                min_len = min(min_len, i2 - i1 + 1)
                cur_sum -= nums[i1]
                i1 += 1
                
            else:
                if i2 < length - 1:
                    i2 += 1
                    cur_sum += nums[i2]
                else:
                    break
                    
        return 0 if min_len == float('inf') else min_len
                
                
'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Solution: Two pointers, move t1 forward when sum is larger than target, else move t2 forward, update the current sum between [t1, t2+1]
Time, Space: O(n)
'''
