class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max([self.find_max(nums[1:]), self.find_max(nums[:-1])])
        
    def find_max(self, nums):
        dp = [[0, 0]]
        for n in nums:
            prev = dp[-1]
            cur = [max(prev), prev[0] + n]
            dp.append(cur)
        return max(dp[-1])

    
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Solution: DP, Greedy
    - Since the houses are in a circle, at least of 1 cannot be robbed from (head, tail)
    - calculate max value twice, without head or tail
Time: O(n)
Space: can be O(1)
'''
