class Solution(object):
    def isPalindrome(self, x):
        st=str(x)
        count=0
        while(count<len(st)/2):                                 #convert number into string and count the same numbers
            if(st[count]==st[len(st)-count-1]):
                count+=1
            else:
                break
        if(count==len(st)/2):                                  #To check if this number is a palindrome number
            return True
        else:
            return False
            
        """
        :type x: int
        :rtype: bool
        """
        
