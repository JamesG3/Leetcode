class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        
        t_dic = {}
        for c in t:
            t_dic[c] = t_dic.get(c, 0) + 1
        
        # sliding window candidates
        check = []
        for i, c in enumerate(s):
            if c in t_dic:
                check.append([i, c])
        
        required = len(t_dic)
        matched = 0
        window = {}
        l = 0
        # cur_min_length, cur_start, cur_end
        res = [float('inf'), None, None]
        
        # travesrse all candidates as the right pointer
        for i, c in check:
            window[c] = window.get(c, 0) + 1
            if window[c] == t_dic[c]:
                matched += 1
            
            # when qualified, move left pointer to minimize the size of sliding window
            while l <= i and matched == required:
                start, end = check[l][0], i
                if end - start + 1 < res[0]:
                    res = [end - start + 1, start, end]
                window[check[l][1]] -= 1
                if window[check[l][1]] < t_dic[check[l][1]]:
                    matched -= 1        
                l += 1
        
        return '' if res[0] == float('inf') else s[res[1]: res[2] + 1]

    
'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Solution: Hashtable, sliding window, two pointers
Time: O(n) -> len(s) + len(t)
Space: O(n) -> len(s) + len(t)
'''
    
    

