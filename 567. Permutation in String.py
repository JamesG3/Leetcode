class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1cnter = {}
        for c in s1:
            s1cnter[c] = s1cnter.get(c, 0) + 1
        
        s2cnter = {}
        s2cnter_sze = 0
        for i, c in enumerate(s2):
            if s2cnter_sze == len(s1):
                if s2cnter == s1cnter:
                    return True
                rm_c = s2[i-len(s1)]
                s2cnter[rm_c] -= 1
                if s2cnter[rm_c] == 0:
                    del s2cnter[rm_c]
                    
                s2cnter[c] = s2cnter.get(c, 0) + 1
                
            else:
                s2cnter_sze += 1
                s2cnter[c] = s2cnter.get(c, 0) + 1
                
        return s1cnter == s2cnter
        
'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Solution: Sliding window, hash table, edge case, 
Time: O(max(len(s1), len(s2)))
Space: O(1), 26 letters total
'''
