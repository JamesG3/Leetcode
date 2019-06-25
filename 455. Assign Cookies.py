class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        Solution: Greedy
        Time: O(nlgn)
        Space: O(1)
        """
        g.sort()
        s.sort()
        
        i, j = 0, 0
        g_len, s_len = len(g), len(s)
        res = 0
        
        while True:
            if i == g_len or j == s_len:
                break
                
            if s[j] >= g[i]:
                res += 1
                j += 1
                i += 1          
            else:
                j += 1
                
        return res
            
        
        
"""
Example:
Input: [1,2,3], [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

You may assume the greed factor is always positive. 
You cannot assign more than one cookie to one child.
"""
