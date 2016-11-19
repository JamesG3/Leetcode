class Solution(object):
    def isPalindrome(self, s):
        if len(s)==0:
            return True
            
        left=0
        right=len(s)-1
        
        while left<right:
            while left<right and not s[left].isalnum():     #find valid alphanumeric in order
                left+=1
            while left<right and not s[right].isalnum():    #find valid alphanumeric in reverse order
                right-=1
                
            if s[left].lower()!=s[right].lower():       #if current character don't have a corresponding palindrome charachter
                return False
            left+=1
            right-=1
            
        return True
            
        
        """
        Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
        For example,
        "A man, a plan, a canal: Panama" is a palindrome.
        
        :type s: str
        :rtype: bool
        """     


"""
# a brute force solution, will cause a TLE error
class Solution(object):
    def isPalindrome(self, s):
        if len(s)==0:
            return True
        S1=""
        S2=""
        left=0
        right=len(s)-1
        
        for n in s:
            if s[left].isalnum():
                S1+=s[left]
            if s[right].isalnum():
                S2+=s[right]
                
            left+=1
            right-=1
            
        return S1.lower()==S2.lower()
        
        """
        
