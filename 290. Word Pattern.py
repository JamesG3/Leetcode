class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(' ')
        paten = {}
        rev_paten = {}
        
        if len(words) != len(pattern):
            return False
        
        for i, c in enumerate(pattern):
            w = words[i]
            if (w in rev_paten and c not in paten) or (w not in rev_paten and c in paten):
                return False
            elif c not in paten:
                paten[c] = w
                rev_paten[w] = c
            else:
                if paten[c] != w:
                    return False
                
        return True
                
        
'''
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Solution: Hashtable, create mapping relation and reversed mapping relation (two dictionaries)
Time: O(n)
Space: O(n)
'''
