class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        p1, p2 = 0, 0
        len1, len2 = len(A), len(B)
        
        if not len1 or not len2:
            return res
        
        inter1, inter2 = None, None
        while p1 < len1 and p2 < len2:
            inter1 = A[p1]
            inter2 = B[p2]

            interval = self.find_interval(inter1, inter2)
            if interval:
                res.append(interval)
            if inter1[-1] > inter2[-1]:
                p2 += 1
            else:
                p1 += 1
    
        return res
                   
            
    def find_interval(self, in1, in2):
        if in1[0] > in2[-1] or in2[0] > in1[-1]:
            return []
        
        if in1[0] > in2[0]:
            return [in1[0], min(in1[-1], in2[-1])]
        
        else:
            return [in2[0], min(in1[-1], in2[-1])]
            
            
'''
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)


Solution: Two pointers, Greedy
Time: O(n)
Space: O(n)
'''
