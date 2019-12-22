class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        length = len(s)
        max_len = 0
        
        if length < 2:
            return length
        
        dic = {}
        l, r = 0, 0
        max_len = 0
        while r < length:
            if s[r] in dic:
                dic[s[r]] = r
            else:
                if len(dic) == 2:
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
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Solution: two pointers, sliding window, use hashmap to save the leftmost index of each distinct element
Time & Space: O(n)
'''
