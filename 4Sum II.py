class Solution(object):
    def fourSumCount(self, A, B, C, D):
        dic = {}
        counter = 0
        for n in A:                 #calculate the sum for each pair of numbers in A and B
            for m in B:
                if m+n in dic:
                    dic[m+n] += 1
                else:
                    dic[m+n] = 1
                    
        for i in C:                 #calculate sums in C and D
            for j in D:
                if -(i+j) in dic:
                    counter += dic[-(i+j)]
        
        return counter
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        # Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
        # To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
        
