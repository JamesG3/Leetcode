class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palin(i, j):
            return all([s[k] == s[j-k+i] for k in range(i, j)])
        
        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return check_palin(i+1, j) or check_palin(i, j-1)
        return True

'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Solution: Two pointers
Time: O(n)
Space: O(1)
'''
        
        
        
