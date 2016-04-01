class Solution(object):
    def isValid(self, s):
            L = ["[", "{", "("]
            R = ["]", "}", ")"]
            stack = []
            
            for c in s:
                if c in L:                                              #if c is [ { (, keep append stack
                    stack.append(c)
                
                if c in R:
                    if len(stack) == 0:
                        return False
                    if(L.index(stack.pop()) != R.index(c)):             #compare the left part and the right part,and pop the right elements
                        return False
                        
            if len(stack) > 0:                                          #if there is still element left in the stack,false
                return False
                
            return True



#