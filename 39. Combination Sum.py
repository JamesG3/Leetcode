class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.length = len(candidates)
        self.res = []
        self.candidates = sorted(candidates)
        self.helper(target, 0, [])
        return self.res
        
    def helper(self, target, candi_i, cur_res):
        if target == 0:
            self.res.append(cur_res)
            return
        
        for i in range(candi_i, self.length):
            if target - self.candidates[i] < 0:
                return
            
            self.helper(target - self.candidates[i], i, cur_res + [self.candidates[i]])
            
'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Solution: DFS
Time: O(n^2)
'''
