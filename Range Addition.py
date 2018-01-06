class Solution(object):
    def getModifiedArray(self, length, updates):
        res = [0] * length
        
        for item in updates:
            head, tail, add = item[0], item[1], item[2]
            
            res[head] += add            # start add from index 'head'
            if tail+1 < length:         # if tail is not the last number in list
                res[tail + 1] -= add    # cancel add from index 'tail+1'
        
        for i in xrange(1, length):     # add iteratively
            res[i] += res[i-1]
            
        return res
        
        
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        
        # Assume you have an array of length n initialized with all 0's and are given k update operations.
        # Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
        # Return the modified array after all k operations were executed.
