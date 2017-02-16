class Solution(object):
    def convertToBase7(self, num):
        max = 0
        bit = 0
        mark = 0
        
        if num == 0:
            return "0"
        if num<0:
            num = -num
            mark = 1
        
        while num >= 7**bit:
            bit+=1
        ans = ""
        for i in xrange(bit-1,-1,-1):
            
            apen = num/7**i
            ans+=str(apen)
            num-=apen*7**i
            
        if mark == 1:
            return "-"+ ans
        return ans
        
        """
        :type num: int
        :rtype: str
        """
        
        #Given an integer, return its base 7 string representation.
