class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        
        # start traverse from head
        for i in range(length):
            # when i == j, palind_length = 1
            dp[i][i] = 1
            # traverse from tail, prevent collision when i == j
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    # when i != j but s[i] == s[j], palind_length += 2
                    dp[i][j] = dp[i-1][j+1] + 2
                else:
                    # get the max previous status from two direction
                    dp[i][j] = max(dp[i][j+1], dp[i-1][j])
        return dp[-1][0]
'''
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Solution: DP, For each length of subarray, get the dup count by comparing head and tail, then pass the max count to next state, accumulate the count until full length is compared
Time, Space: O(n^2)
'''    
                
