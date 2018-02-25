class Solution(object):

    # two pointers solution
    def reverseStr(self, s, k):
        s = list(s)
        length = len(s)
        for n in xrange(length/k + 1):
            if n%2 == 0:
                i, j = n*k, min((n+1)*k-1, length-1)
                while i<j:
                    s[i], s[j] = s[j], s[i]
                    i+=1
                    j-=1
                
        return "".join(s)
        
        
        
        
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        # Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. 
        # If there are less than k characters left, reverse all of them. 
        # If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
        
