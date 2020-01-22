from collections import defaultdict

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        dic = defaultdict(set)
        
        # for each combination of elements
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:]):
                dic[m+n].add(tuple([(m, j+i+1), (n, i)]))
        ans = set()
        for k, v in dic.items():
            part2 = target - k
            if part2 not in dic:
                continue
                
            v2 = dic[part2]
            for v_1 in v:
                for v_2 in v2:
                    # use index to prevent duplicate elements appear in the same answer
                    ans_index = [v_1[0][1], v_1[1][1], v_2[0][1], v_2[1][1]]
                    if len(set(ans_index)) == 4:
                        ans.add(tuple(sorted([v_1[0][0], v_1[1][0], v_2[0][0], v_2[1][0]])))
        return list(ans)
            
'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Solution: Hashtable, array
Time: O(n^2)
Space: O(n^2)
'''    
        
