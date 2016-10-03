class Solution(object):
    def plusOne(self, digits):
        n=-1
        while n != -len(digits)-1 and digits[n]+1 >= 10:
            digits[n] = (digits[n]+1)%10
            n-=1
        if n != -len(digits)-1:
            digits[n]+=1
        else:
            digits=[1]+digits
        return digits
            
        """
        :type digits: List[int]
        :rtype: List[int]
        
        Given a non-negative number represented as an array of digits, plus one to the number.
        The digits are stored such that the most significant digit is at the head of the list.
        """
        
