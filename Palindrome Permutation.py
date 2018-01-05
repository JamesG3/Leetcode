class Solution(object):
    def canPermutePalindrome(self, s):
        dic = {}
        for letter in s:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
            
        flag = 0
        for item in dic:
            if dic[item]%2 != 0:
                flag += 1
                
        return flag < 2
                
        
        
        """
        :type s: str
        :rtype: bool
        """
        
        # Given a string, determine if a permutation of the string could form a palindrome.


        
        
        
        
        
