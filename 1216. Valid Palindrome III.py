class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        if not s:
            return True
        
        self.dp = {}
        self.s = s
        self.helper(0, len(s))
        return self.dp[(0, len(s))] <= k 
        
        
    def helper(self, l, r):
        if l == r or l+1 == r:
            return 0
        
        if (l, r) in self.dp:
            return self.dp[(l, r)]
        
        if self.s[l] == self.s[r-1]:
            self.dp[(l, r)] = self.helper(l+1, r-1)
        else:
            self.dp[(l, r)] = min(self.helper(l+1, r), self.helper(l, r-1)) + 1
        
        return self.dp[(l, r)]

    
'''
Given a string s and an integer k, find out if the given string is a K-Palindrome or not.
A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.

Solution: DP, hash table, edge case
Time: O(n^2)
Space: O(n^2)
'''
