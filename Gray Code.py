class Solution(object):
    def grayCode(self, n):
        ans=[0]
        for n in range(0,n):
            tem=[]
            for m in ans:
                tem.append(m+2**n)
            ans+=tem[::-1]
         
        return ans
        
        """
        :type n: int
        :rtype: List[int]
        """
        
