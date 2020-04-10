class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        cnter = {}
        p1, p2 = 0, 0
        res = 0
        cur_length = 0
        
        if k == 0:
            return 0
        
        while p2 < len(s):
            cnter[s[p2]] = cnter.get(s[p2], 0) + 1
            cur_length += 1
            p2 += 1
            
            if len(cnter) > k:
                res = max(res, cur_length-1)
                while len(cnter) > k:
                    cnter[s[p1]] -= 1
                    cur_length -= 1
                    if cnter[s[p1]] == 0:
                        del cnter[s[p1]]
                    p1 += 1
        
        return max(cur_length, res)
                    
'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Solution: Sliding window, hash table, two pointers
Time, Space: O(n)
'''                
