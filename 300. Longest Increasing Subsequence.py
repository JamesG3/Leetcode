class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        p = len(nums) - 1
        dp = [1 for _ in nums]
        
        while p > -1:
            max_cnt = 1
            for i in range(p+1, len(nums)):
                if nums[i] > nums[p]:
                    max_cnt = max(max_cnt, dp[i] + 1)
                dp[p] = max_cnt    
            p -= 1
        return max(dp) if dp else 0
                
                
'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Solution: DP
Time: O(n^2)
Space: O(n)
'''
