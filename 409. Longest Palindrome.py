from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        res = 0
        for k,v in cnt.items():
            reduced_v = v // 2 * 2
            res += reduced_v
            if res % 2 == 0 and v % 2 == 1:
                res += 1
                
        return res

'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Note:
Assume the length of given string will not exceed 1,010.

Solution: Hashtable, greedy
Time, Space: O(n)
'''
