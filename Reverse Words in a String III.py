class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wlist = s.split(' ')
        return ' '.join([w[::-1] for w in wlist])
        
        
        
        
        """
        Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
        Input: "Let's take LeetCode contest"
        Output: "s'teL ekat edoCteeL tsetnoc"
        Note: In the string, each word is separated by single space and there will not be any extra space in the string.
        """