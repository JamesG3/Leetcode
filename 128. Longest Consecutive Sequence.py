class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        res = 0
        
        for num in numsset: 
            # here is the trick to make it O(n), traverse from the smallest element from each interval
            if num-1 not in numsset:
                tmp_res = 0
                cur_num = num
                
                # find how many consecutive number after this num
                while cur_num in numsset:
                    tmp_res += 1
                    res = max(res, tmp_res)
                    cur_num += 1
        return res
    
'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.

Solution: Hashset, Hash table
Time: O(n)
SpaceL: O(n)
'''
