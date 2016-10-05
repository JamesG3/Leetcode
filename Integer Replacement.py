class Solution(object):
    def integerReplacement(self, n):
        count=0
        while n != 1:
            if n%2 == 0:
                n=n/2
            else:
                if (n-1)/2 % 2 == 0:           #if (n-1)/2 % 2 == 0 and (n+1)/2 % 2 != 0:   (half of this sentence actually useless, cause (n-1)/2 %2 means that (n+1)/2 %2 !=0)
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
        
        Given a positive integer n and you can do operations as follow:
        If n is even, replace n with n/2.
        If n is odd, you can replace n with either n + 1 or n - 1.
        What is the minimum number of replacements needed for n to become 1?
        """
        
