class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = [[nums[0], nums[0]]]
        for i, n in enumerate(nums[1:]):
            if n - res[-1][-1] == 1:
                res[-1][-1] = n
            else:
                res.append([n, n])
            
        return ['{}->{}'.format(l[0], l[1]) if l[0] != l[1] else str(l[0]) for l in res]
        
'''
Given a sorted integer array without duplicates, return the summary of its ranges.
Example: 
    Input:  [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Solution: Traverse and mark
Should be an easy one
'''
