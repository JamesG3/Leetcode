from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_cnt = Counter(p)
        s_len = len(s)
        p_len = len(p)
        res = []
        
        if s_len < p_len:
            return []
        
        sub_s = s[:p_len]
        cur_cnt = Counter(sub_s)
        if cur_cnt == p_cnt:
            res.append(0)
        for i in range(s_len - p_len):
            cur_cnt[s[i]] -= 1
            if cur_cnt[s[i]] == 0:
                del cur_cnt[s[i]]
                
            cur_cnt[s[p_len + i]] += 1
                
            if cur_cnt == p_cnt:
                res.append(i + 1)
        
        return res

    
'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Solution: Hashtable, Counter, be careful about the optimization
Space, Time: O(n)
'''
