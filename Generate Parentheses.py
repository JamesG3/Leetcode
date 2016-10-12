class Solution(object):
    def generateParenthesis(self, n):
        
        ans=[]
        
        def generate(n,count,String):                       #recursive function
            if count>0:                                     
                generate(n,count-1,String + ")")
            if n>0:
                generate(n-1,count+1,String + "(")
            elif n==0 and count==0:                         #append string to ans when a result generated
                ans.append(String)
        
        generate(n,0,"")
        
        return ans[::-1]
                
        """
        :type n: int
        :rtype: List[str]
        
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
        For example, given n = 3, a solution set is:
        ["((()))","(()())","(())()","()(())","()()()"]
        """
        
