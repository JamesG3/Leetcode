class Solution(object):
    
    # two pointers solution
    class Solution(object):
    def strStr(self, haystack, needle):
        n_length = len(needle)
        h_length = len(haystack)

        if h_length <= 1:
            if haystack == needle:
                return 0
            
            elif h_length and not n_length:
                return 0
            else:
                return -1
        p1 = 0
        flag = 0
        while p1 < h_length:
            if haystack[p1] == needle[0]:
                if h_length - p1 >= n_length:
                    flag = 0
                    for i in xrange(p1, p1+n_length):
                        if haystack[i] != needle[i-p1]:
                            flag = 1
                            break
                    if i-p1 == n_length-1 and not flag:
                        return p1
                else:
                    return -1
            p1 += 1            
        return -1
                    

        
    
    
    
    
    
    # simple solution
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        return -1
        
        
        
        """
        Implement strStr().
        Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
