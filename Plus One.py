class Solution(object):
    def plusOne(self, digits):
        carry = 1
            
        for i in xrange(len(digits)-1, -1, -1):
            if digits[i] + carry == 10:
                digits[i] = 0
            else:
                digits[i] = digits[i] + carry
                carry = 0
                
        if carry == 1:
            return [1] + digits
        else:
            return digits
            
        """
        :type digits: List[int]
        :rtype: List[int]
        
        Given a non-negative number represented as an array of digits, plus one to the number.
        The digits are stored such that the most significant digit is at the head of the list.
        """
        
