class Solution(object):
    def reverseBits(self, n):
        tem= bin(n)
        L=len(tem)-2
        i=-1
        new=''
        for i in range(1,33):
            if(i<=L):
                new+=tem[-i]
            else:
                new+='0'
        
        return int(int(new, 2))
        
        """
        :type n: int
        :rtype: int
        """
        #Reverse bits of a given 32 bits unsigned integer.
