class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def helper(used, left):
            if not left:
                res.add(tuple(used))
            else:
                for i, n in enumerate(left):
                    helper(used + [n], left[:i] + left[i+1:])
        helper([], nums)
        return [list(t) for t in res]
    
    
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Solution: Backtracking, Hashset
'''
