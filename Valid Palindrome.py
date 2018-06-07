class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            
            if not s[r].lower() == s[l].lower():
                return False
            else:
                l += 1
                r -= 1
        
        return True    
        
            
        
        """
        Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
        For example,
        "A man, a plan, a canal: Panama" is a palindrome.
        
        :type s: str
        :rtype: bool
        """     

