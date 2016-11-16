class Solution(object):
    def repeatedSubstringPattern(self, str):
        if len(str)<2:
            return False
        #if len(str)==str.count(str[0]):    supposed to check same element string, but find out it's even slower  
         #   return True
        for n in range(1, len(str)+1):
            if len(str)%n != 0:             #find a possible substring by it's length
                continue
            if self.check(str,n):           #if this is a true substring, return True, if not, continue
                return True
        return False
            
    def check(self, str, n):                #check this possible substring
        sub=str[0:n]
        j=n
        k=2*n
        l=len(str)
        if n==l:
            return False
        while j != l:
            if sub != str[j:k]:
                return False
            j+=n
            k+=n
        return True
            
        
        """
        Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 
        You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
        
        :type str: str
        :rtype: bool
        """
