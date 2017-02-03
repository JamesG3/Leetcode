class Solution(object):
    def longestPalindrome(self, s):
        d={}
        even=0
        odd=0
        for n in s:             #count the number of every letter
            if n in d:
                d[n]+=1
            else:
                d[n]=1
                
        for n in d:
            if d[n]%2==0:           #if the number of a letter is even, then all of them can be used in the Palindrome
                even+=d[n]
            else:                   #if it's odd
                if d[n]>odd:        #always choose the larger one, the largest odd letters can be put in the middle of the Palindrome
                    if odd != 0:    #if the former largest odd is replaced, then add it to even with value (odd-1)
                        even += odd-1
                    odd=d[n]        #replace it
                
                else:               #if small than the current largest odd, then add it to even with value (odd-1)
                    if d[n] != 1:
                        even+=d[n]-1
                        
        return odd+even
        
        """
        :type s: str
        :rtype: int
        """
        
        
        #Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
