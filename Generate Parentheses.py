class Solution(object):
    def generateParenthesis(self, n):
        
        ans=[]
        
        def generate(n,count,String):
            if count>0:
                generate(n,count-1,String + ")")
            if n>0:
                generate(n-1,count+1,String + "(")
            elif n==0 and count==0:
                ans.append(String)
        
        generate(n,0,"")
        return ans[::-1]
                
        """
        :type n: int
        :rtype: List[str]
        """
        
