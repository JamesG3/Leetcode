class Solution(object):
    def findComplement(self, num):
        multiple = math.log(num, 2)
        ceil = math.floor(multiple) + 1
        
        if num == int(2**ceil-1):
            return 0
        else:
            return int(2**ceil-1-num)
        """
        :type num: int
        :rtype: int
        """
        
        #Given a positive integer, output its complement number. 
        #The complement strategy is to flip the bits of its binary representation.
