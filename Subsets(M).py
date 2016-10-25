class Solution(object):
    def subsets(self, nums):
        if nums==None:
            return []
        elif nums==[]:
            return [[]]
            
        res=[]
        
        self.helper(nums,[],res,0)
        return res
        
    def helper(self,nums,tmp,res,i):
        
        if i==len(nums):
            res.append(tmp[:])
            
           # print "re"
           # print res
            return
        
        self.helper(nums,tmp,res,i+1)
        tmp.append(nums[i])
        self.helper(nums,tmp,res,i+1)
        tmp.remove(tmp[-1])
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        Given a set of distinct integers, nums, return all possible subsets.
        Note: The solution set must not contain duplicate subsets.
        """
        
