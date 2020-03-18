class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.res = 0
        self.arr = arr
        self.dfs(0,"")
        return self.res
    
    def valid(self, s):
        return len(s) == len(set(s))
        
        
    def dfs(self,i,ans):
        for j in range(i, len(self.arr)):
            new_str = ans + self.arr[j]
            if not self.valid(new_str):
                continue
                
            self.res = max(self.res, len(new_str))
            self.dfs(j+1,new_str)
    
'''
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.
Return the maximum possible length of s.

Solution: DFS, backtracking
'''




