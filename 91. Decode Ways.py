class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        # bottom up, the dp[-1] should be 1, the dp[-2] should be 0 if it's '0'
        dp = [0 for _ in range(len(s) - 1)] + [int(s[-1] != '0'), 1]
        
        # traverse from the s[-2] to s[0]
        for i in range(len(s) - 2, -1, -1):
            # if there are two successive '0', then the result would be 0
            if s[i] == '0':
                continue
            # not possible to generate new possiblity
            if int(s[i:i+2]) > 26:
                dp[i] = dp[i+1]
            # add up the two previous possibilities
            else:
                dp[i] = dp[i+1] + dp[i+2]
        
        return dp[0]
            
            
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Solution: DP, Bottom up, Backtracking
Time, Space: O(N)
'''
        
