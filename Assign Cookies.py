class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        counter=0
        while len(s)!=0 and len(g)!=0:
            if s[0]<g[0]:
                del s[0]
            else:
                del s[0]
                del g[0]
                counter+=1
        return counter
        
        """
        Example:
        Input: [1,2,3], [1,1]
        Output: 1
        Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
        And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
        You need to output 1.
        
        You may assume the greed factor is always positive. 
        You cannot assign more than one cookie to one child.
        
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
