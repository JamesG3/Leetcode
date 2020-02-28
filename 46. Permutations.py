class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def helper(used, left):
            if len(left) == 0:
                ans.append(used)
            for i, n in enumerate(left):
                helper(used + [n], left[:i] + left[i+1:])
        
        helper([], nums)
        return ans
                
'''
Given a collection of distinct integers, return all possible permutations.

Solution: Backtracking, Recursive, BFS
Space: O(n!)
'''
