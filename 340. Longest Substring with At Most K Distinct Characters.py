class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        length = len(s)
        max_len = 0
        
        if k == 0:
            return 0
        
        if length < k:
            return length
        
        dic = {}
        l, r = 0, 0
        max_len = 0
        while r < length:
            if s[r] in dic:
                dic[s[r]] = r
            else:
                if len(dic) == k:
                    max_len = max(max_len, r - l)
                    l = self.remove_leftmost(dic)
                dic[s[r]] = r
            r += 1
                    
        return max(max_len, r - l)
    
    
    def remove_leftmost(self, dic):
        rev_dic = {v:k for k,v in dic.items()}
        leftmost = min(rev_dic)
        del dic[rev_dic[leftmost]]
        return leftmost + 1
    
    
'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Solution:   Two pointers, sliding window
            exactly same solution as 159. Longest Substring with At Most Two Distinct Characters
            but need to do some specal handling when (k == 0)
            
Time, Space = O(n)
'''
