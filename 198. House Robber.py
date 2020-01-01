class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0, 0]]
        for n in nums:
            prev = dp[-1]
            cur = [max(prev), prev[0]+n]
            dp.append(cur)
            
        return max(dp[-1])

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Solution: DP
    Save these two results at the top of stack: [max value if do not rob the current one, max value if rob the current one]
    
Time: O(n)
Space can be: O(1), only need to save the previous snapshot
'''
