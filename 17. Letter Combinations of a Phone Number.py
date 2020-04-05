class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        return [_ for _ in self.helper(digits, '')]
        
        
        
    def helper(self, remain, cur_str):
        if not remain:
            if cur_str:
                yield cur_str
            return
            
        candis = self.mapping[remain[0]]
        for candi in candis:
            yield from self.helper(remain[1:], cur_str + candi)
            
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Solution: DFS, backtracking
Time: O(n)
Space: O(n)
'''
