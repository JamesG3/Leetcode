class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        Two pointers solution
        Time: O(n)
        Space: O(n)
        """
        if not A:
            return A
        
        length = len(A)
        width = len(A[0])
        
        for i in xrange(length):
            h, t = 0, width - 1
            while h <= t:
                A[i][h], A[i][t] = 1 ^ A[i][t], 1 ^ A[i][h]
                h += 1
                t -= 1
        return A
        
# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].





