class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        
        Stack solution, use flag to mark if in the outer parentheses
        Time: O(n)
        Space: O(n)
        """
        flag = 0
        stack = []
        res = ''
        
        
        for c in S:
            if flag == 0:
                flag = 1
                continue
            else:
                if not stack:
                    if c == ')':
                        flag = 0
                    else:
                        stack.append(c)
                        res += c
                else:
                    if c == '(':
                        stack.append(c)
                    else:
                        stack.pop()
                    res += c
                    
        return res
                
        # A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
        # A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
        # Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
        # Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
