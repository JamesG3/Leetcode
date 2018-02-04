class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')
        
        
#         if x == y:
#             return 0
        
#         x_bin = bin(x)[2:]
#         y_bin = bin(y)[2:]          #transform to binary
        
#         x_len = len(x_bin)
#         y_len = len(y_bin)
        
#         if x_len > y_len:           #fix length
#             y_bin = '0'*(x_len - y_len) + y_bin
#         elif y_len > x_len:
#             x_bin = '0'*(y_len - x_len) + x_bin
        
#         counter = 0
#         index = 0
#         while index != max(x_len, y_len):       #compare each digit
#             if x_bin[index] != y_bin[index]:
#                 counter+=1
#             index+=1
#         return counter
        
                                        #To save time, we can compare from the fist digit of the shorter one, then add this number with the count of character '1' of the rest part.
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        
        #The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
        #Given two integers x and y, calculate the Hamming distance.
