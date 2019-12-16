class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_seen = {c: i for i,c in enumerate(s)}
        visted = {}
        
        for i,c in enumerate(s):
            if c not in visted:
                while stack and c < stack[-1] and last_seen[stack[-1]] > visted[stack[-1]]:
                    d = stack.pop()
                    del visted[d]
                stack.append(c)
                visted[c] = i
            
            # if already visted, update the traverse index to the current index
            # or 'b' will be totally removed from str like 'bbacd'
            else:
                visted[c] = i
                
        return ''.join([_ for _ in stack])
                    
'''
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Solution: Stack
Time & Space: O(n)
'''
