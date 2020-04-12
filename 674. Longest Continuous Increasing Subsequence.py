class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = 0
        cur_res = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur_res += 1
                
            else:
                res = max(res, cur_res)
                cur_res = 1
        
        return max(cur_res, res)
            
'''
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Solution: Traverse & mark
Time: O(n)
Space: O(n)
'''
