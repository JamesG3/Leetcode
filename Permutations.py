class Solution(object):
    
    # backtrack solution
    def permute(self, nums):
        length = len(nums)
        if length == 0:
            return [[]]
        ans = []
        
        def backtrack(l):
            if len(l) == length:
                ans.append(l[:])
                
            for n in nums:
                if n in l:
                    continue
                l.append(n)
                backtrack(l)
                l.pop()
                
        backtrack([])
        return ans
            
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #Given a collection of distinct numbers, return all possible permutations
        #For example,
        #[1,2,3] have the following permutations:
        #[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1]. 
