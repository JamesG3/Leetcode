class Solution(object):
    def findPermutation(self, s):
        length = len(s)
        stack = []
        res = []
        
        num = 1         # current number
        i = 0           # index for s
        curr = s[0]     # the first order in s
        
        while i < length:
            if curr != s[i]:    # if change
                curr = s[i]
                
                if s[i] == "I":     # if D to I
                    stack = [num] + stack   # push the last number to stack
                    res += stack            # append the stack to res
                    stack = []              # clear stack
                    
                    num += 1
                    i += 1
                    continue
                    
            
            if s[i]  == "D":            # if decrease, push current number to stack
                stack = [num] + stack
                    
            else:                       # if increase, append current number to res
                res.append(num)
                
            num += 1
            i += 1 
        
        if s[-1] == "D":                # apply the same rule to the last number
            stack = [num] + stack
            res += stack
        else:
            res += [num]
            
            
        return res
    
    
        """
        :type s: str
        :rtype: List[int]
        """
        
