class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[0 for _ in range(len1+1)] for _ in range(len2+1)]
        if not dp or not dp[0]:
            return 0
        
        for i in range(len2):
            for j in range(len1):
                if text1[j] == text2[i]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[-1][-1]
                    
'''
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
If there is no common subsequence, return 0.

Solution: DP, DP[i][j] = DP[i-1][j-1]+1 , if text1[i] == text2[j] DP[i][j] = max(DP[i-1][j], DP[i][j-1]), otherwise
Time: O(n*m)
Space: O(n*m)
'''
