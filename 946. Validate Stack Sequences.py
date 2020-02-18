class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        p_i = 0
        for n in pushed:
            stack.append(n)
            while stack and stack[-1] == popped[p_i]:
                stack.pop()
                p_i += 1
        
        return p_i == len(popped)
            
'''
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

Solution: Stack, Simulation
Time: O(n)
Space: O(n)
'''    
        
