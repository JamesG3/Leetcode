from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        cnter = Counter(S)
        max_cnt = max(cnter.values())
        rest_cnt = len(S) - max_cnt
        # check if it's possible to reorganize this string
        if max_cnt - rest_cnt >= 2:
            return ''
        
        cnter_q = [[-v, k] for k, v in cnter.items()]
        heapq.heapify(cnter_q)
        
        res = ''
        # early terminatin if res reach the length
        while len(cnter_q) >= 2 and len(res) != len(S):
            # get top 2 chars from heap, append to res string
            n1, c1 = heapq.heappop(cnter_q)
            n2, c2 = heapq.heappop(cnter_q)
            
            # push the char back to heap with count-1
            if n1:
                res += c1
                heapq.heappush(cnter_q, [n1+1, c1])
            
            if n2:
                res += c2
                heapq.heappush(cnter_q, [n2+1, c2])
        return res
                
'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.

Solution: Priority queue, Math, heap
Time: O(nlogm)
'''        
