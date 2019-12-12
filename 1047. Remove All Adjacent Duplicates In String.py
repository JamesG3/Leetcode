class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        length = 0
        
        for c in S:
            has_dup = False
            
            while length > 0 and stack[-1] == c:
                has_dup = True
                stack.pop()
                length -= 1
                
            if not has_dup:
                stack.append(c)
                length += 1
                
        return ''.join(stack)
    
'''
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

Solution: Stack
Time & Space: O(n)
'''
