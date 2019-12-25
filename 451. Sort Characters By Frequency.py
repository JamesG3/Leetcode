from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt_dic = Counter(s)
        lst = [[k,v] for k,v in cnt_dic.items()]
        return ''.join([k*v for k,v in sorted(lst, key = lambda x:x[1], reverse = True)])
        
'''
Given a string, sort it in decreasing order based on the frequency of characters.

Solution: Hashtable
Time: O(nlog(n)) - sorting
Space: O(n)
'''
