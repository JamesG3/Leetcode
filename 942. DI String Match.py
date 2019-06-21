class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
    
        Solution: two pointers
        Time: O(n)
        SpaceL O(n)
        """
        low, high = 0, len(S)
        res = []
        
        for c in S:
            if c == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
                
        return res + [high]
        
        
# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]
