class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        
        i = 0
        length = len(bits) - 1
        while i < length:
            i += bits[i] + 1
            
        return i == length
        
        
        
        
        """
        Using the 1/0 characteristic to update i incrementally
        If bits[i] == 1: jump to next 2-bits Char
        If bits[i] == 0: to next 1-bit Char
        """