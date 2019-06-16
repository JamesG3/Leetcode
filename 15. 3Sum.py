from collections import Counter

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution = set([])
        dic = Counter(nums)
        
        for i in dic:
            for j in dic:
                if i==j and dic[i] < 2:
                    continue
                    
                k = -(i+j)
                if k not in dic:
                    continue
                    
                if j==i==k and dic[k] < 3:
                    continue
                    
                if (j==k or i==k) and dic[k] < 2:
                    continue
                    
                Solution.add(tuple(sorted([i, j, k])))
                
        return list(Solution)
                    
        # Hashmap solution
        # O(n^2) solution, depends on the size of dic
        # friendly if there are many dup elements in the nums
