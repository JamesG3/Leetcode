class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        counter = 0
        length = len(chars)
        
        write = curstart = 0
        for i, c in enumerate(chars):
            if i == length-1 or chars[i+1] != c:
                chars[write] = chars[curstart]
                write += 1
                if i > curstart:
                    for n in str(i-curstart+1):
                        chars[write] = n
                        write += 1
                curstart = i+1
                    
        return write
            
            
# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.
# Could you solve it using only O(1) extra space?

