class Solution(object):
    def integerReplacement(self, n):
        count=0
        while n != 1:
            if n%2 == 0:
                n=n/2
            else:
                if (n-1)/2 % 2 == 0:           #if (n-1)/2 % 2 == 0 and (n+1)/2 % 2 != 0:
                    n-=1
                elif (n+1)/2 % 2 == 0 and (n+1)/2 < (n-1):  #elif (n-1)/2 % 2 != 0 and (n+1)/2 % 2 == 0 and (n+1)/2 < (n-1):
                    n+=1
                else:
                    n-=1
            count+=1
        return count
        """
        :type n: int
        :rtype: int
        """
        
