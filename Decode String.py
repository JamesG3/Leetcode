class Solution(object):
    def decodeString(self, s):
        mult = 0
        curr = ''
        stack = []
        
        for n in s:
            #print stack
            if n.isdigit():
                mult = mult*10 + int(n)
                
            elif 97<=ord(n)<=122:           #if n is a letter
                curr+=n
                
            elif n == '[':
                stack.append(curr)
                stack.append(mult)
                curr = ''
                mult = 0
                
            #the number of '[' is same as ']', so the the stack will be empty in the end
            
            elif n == ']':
                num = stack.pop()
                prestring = stack.pop()
                curr = prestring + num*curr
                
        return curr
                
        
        """
        :type s: str
        :rtype: str
        """
        
        
        #The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
        #s = "3[a]2[bc]", return "aaabcbc".
        #s = "3[a2[c]]", return "accaccacc".
        #s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
