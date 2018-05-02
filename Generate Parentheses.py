class Solution(object):
    
    
    # backtracking solution, DFS
    def generateParenthesis(self, n):
        res = []
        
        def helper(Length, left, right, S):
            if Length == 2*n:
                res.append(S)
                return
            if left < n:
                helper(Length+1, left+1, right, S+'(')
            if right < left:
                helper(Length+1, left, right+1, S+')')
                
        helper(0, 0, 0, '')
        return res
            
        
        """
        :type n: int
        :rtype: List[str]
        """
        
        
        # Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
        # 3
        # ["((()))","(()())","(())()","()(())","()()()"]
        
