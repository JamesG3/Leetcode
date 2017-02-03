class Solution(object):
    def countSegments(self, s):
        s = s.strip()
        if len(s) == 0:         #edge case: ''
            return 0
            
        mark = 0                #mark for continuous space
        counter = 0
        
        for n in s:
            if n == ' ' and mark == 0:
                mark = 1
                counter += 1
            if n != ' ':
                mark = 0
                
        return counter+1
        """
        :type s: str
        :rtype: int
        """
        
        #Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
        #Please note that the string does not contain any non-printable characters.
