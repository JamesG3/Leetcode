class Solution:
    def convertToTitle(self, n: int) -> str:
        if n == 0:
            return ''
        
        else:
            return self.convertToTitle((n-1) // 26) + chr(ord('A') + (n-1) % 26)
            
'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:
1 -> A
2 -> B
3 -> C
...
26 -> Z
27 -> AA
28 -> AB 
        
Solution: Backtracking, Math
Time: O(n)
'''
        
        
