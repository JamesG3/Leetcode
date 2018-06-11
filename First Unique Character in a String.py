class Solution(object):
    
    # hashtable solution, O(n)
    def firstUniqChar(self, s):
        dic = {}
        
        for i, c in enumerate(s):
            if c in dic:
                dic[c].append(i)
            else:
                dic[c] = [i]
        
        ans = float('Inf')
        for c in dic:
            if len(dic[c]) == 1:
                ans = min(ans, dic[c][0])
                
        return ans if ans != float('Inf') else -1
            
        
        """
        :type s: str
        :rtype: int
        """
        
        # Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

