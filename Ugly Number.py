class Solution(object):
    def isUgly(self, num):
        if(num==0):
            return False
        elif(num==1):
            return True
        else:
            while(num!=1):
                if(num%2==0):
                    num/=2
                elif(num%3==0):
                    num/=3
                elif(num%5==0):
                    num/=5
                
                else:
                    return False
            return True
            
        """
        :type num: int
        :rtype: bool
        """
        
