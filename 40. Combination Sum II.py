class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = set()
        self.helper(sorted(candidates), [], target)
        return list(self.res)
        
    def helper(self, candis, cur_res, remain):
        if remain == 0:
            self.res.add(tuple(cur_res))
            return
        
        if remain < 0:
            return
        
        for i, can in enumerate(candis):
            self.helper(candis[i+1:], cur_res + [can], remain - can)
        
'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Solution: DFS, sort, recursive, backtracking
Time: O(n**2)
'''
