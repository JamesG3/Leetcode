class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        Solution: Greedy, find the largest index for each part of substring
        Time: O(n)
        Space: O(n)
        """
        last_index = {c: i for i,c in enumerate(S)}
        res = []    
        cur_p = 0
        cur_max = 0
        
        for i, c in enumerate(S):
            cur_max = max(cur_max, last_index[c])
            if i == cur_max:
                res.append(i-cur_p+1)
                cur_p = i+1
        
        return res

# A string S of lowercase letters is given. 
# We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
