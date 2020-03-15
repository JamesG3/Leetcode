class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.N = n
        return [_ for _ in self.helper('', 0, 0)]
        
        
    def helper(self, cur_str, left, right):
        if len(cur_str) == 2 * self.N:
            yield cur_str
            
        if left < self.N:
            yield from self.helper(cur_str + '(', left + 1, right)
        if right < left:
            yield from self.helper(cur_str + ')', left, right + 1)

            
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Solution: Backtracking, recursive, generator
'''
