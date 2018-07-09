class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return num%9 if num%9 else 9
        
        
        # Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

