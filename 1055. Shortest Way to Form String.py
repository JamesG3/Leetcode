class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s_i, t_i, s_len, t_len = 0, 0, len(source), len(target)
        counter = 0
        rounds = 0
        
        pre_str = ''
        cur_str = ''
        while t_i < t_len:
            rounds += 1
            for c in source:
                if t_i == t_len:
                    break
                
                if target[t_i] == c:
                    cur_str += c
                    t_i += 1
            
            if cur_str == pre_str:
                return -1
            else:
                pre_str = cur_str
        
        return rounds            
        
'''
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).
Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

Solution: Two pointers
Time: O(m*n)
Space: O(n)
'''
