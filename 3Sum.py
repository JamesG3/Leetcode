





# TLE solution, O(n^2)
from collections import Counter

class Solution(object):
    def threeSum(self, nums):
        res = set()
        dic = Counter(nums)
        
        for n in nums:
            for m in nums:
                if n == m and dic[n] == 1:
                    continue
                k = -(m + n)
                if k not in dic:
                    continue
                    
                if k == m and k == n and dic[k] < 3:
                    continue
                    
                if (k == m or k == n) and dic[k] < 2:
                    continue
                    
                res.add(tuple(sorted([m, n, k])))
        
        return list(res)

        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
