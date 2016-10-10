class Solution(object):
    def grayCode(self, n):
        ans=[0]                         #initial the list
        for n in range(0,n):            #count the times of recursion
            tem=[]                      #use a empty tem list evertime to storage the new appeding part
            for m in ans:
                tem.append(m+2**n)
            ans+=tem[::-1]              #append the tem from end to head
         
        return ans
        
        """
        :type n: int
        :rtype: List[int]
        
        The gray code is a binary numeral system where two successive values differ in only one bit.
        For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
        for n=4, return [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8]
        """
        
