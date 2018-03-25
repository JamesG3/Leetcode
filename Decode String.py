class Solution(object):
    # stack solution
    def decodeString(self, s):
        stack = []
        curr, num = '', ''
        
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append([curr, int(num)])
                curr, num = '', ''
            elif c == ']':
                prev, n = stack.pop()
                curr = prev + curr*n
            else:
                curr+=c
        return curr
                
                
        
        
        """
        :type s: str
        :rtype: str
        """
        
        
        #The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
        #s = "3[a]2[bc]", return "aaabcbc".
        #s = "3[a2[c]]", return "accaccacc".
        #s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
