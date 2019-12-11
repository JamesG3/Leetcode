class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        s, e = 0, length - 1
        
        while s <= e:
            m = (s + e) // 2
            # need to have this to handle exact match, if h-index < count, return the (length - s)
            if citations[m] == length-m:
                return length - m
            
            if citations[m] > length-m:
                e = m - 1
            else:
                s = m + 1
                
        return length - s
        
        
'''
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Solution: Binary Search
Time: O(log(n))
Space: O(1)
'''
