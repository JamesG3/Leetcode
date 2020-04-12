class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pdic = {}
        for c in p:
            pdic[c] = pdic.get(c, 0) + 1
        
        res = []
        cur_res = 0
        cur_dic = {}
        for i, c in enumerate(s):
            if cur_dic == pdic:
                res.append(cur_res)
                cur_dic[s[cur_res]] -= 1
                cur_res += 1
            
            if c not in pdic:
                cur_dic = {}
                cur_res = i + 1
            else:
                if pdic[c] == cur_dic.get(c, 0):
                    while s[cur_res] != c:
                        cur_dic[s[cur_res]] -= 1
                        cur_res += 1
                    cur_res += 1
                    # cur_dic[c] -= 1
            
                else:
                    cur_dic[c] = cur_dic.get(c, 0) + 1
        
        if cur_dic == pdic:
            res.append(cur_res)
            
        return res
    
'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Solution: Hash table, sliding window
Time: O(n)
Space: O(n)
'''
        
