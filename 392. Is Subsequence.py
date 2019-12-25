class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        s_i, t_i = 0, 0
        
        while t_i < t_len:
            if s_i == s_len:
                break
            
            if s[s_i] == t[t_i]:
                s_i += 1
                t_i += 1
            else:
                t_i += 1
        
        return s_i == s_len
        
        
'''
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Solution: greedy, two pointers
Time, Space: O(n)
'''
