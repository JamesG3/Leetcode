class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic = {}
        for i, n in enumerate(A):
            for j, m in enumerate(B):
                dic[m+n] = dic.get(m+n, 0) + 1
        
        counter = 0
        for i, n in enumerate(C):
            for j, m in enumerate(D):
                if -(n+m) in dic:
                    counter += dic[-(n+m)]
       
        return counter
                
'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Solution: Hasttable
Time: O(n^2)
Space: O(n^2)
'''
