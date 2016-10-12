class Solution(object):
    def combinationSum(self, candidates, target):
        if len(candidates)==0:
            return []
        
        candidates.sort()
        res=[]
        tem=[]
        index=0
        self.find(candidates, target, index, res, tem)
        
        return res
        
    
    def find(self, can, tar, index, res, tem):              #calculate all the possible sum
        if tar==0:                                          #save tem to result when one path is right
            res.append(tem)
            return
        if tar < 0:                                         #drop this path when the sum is beyond the target
            return
        else:
            for m in range(index,len(can)):                 #find every path recursively, including repeat numbers
                self.find(can, tar-can[m], m, res, tem+[can[m]])
        
        """
        :type candidates: List[int]a
        :type target: int
        :rtype: List[List[int]]
        
        Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
        The same repeated number may be chosen from C unlimited number of times.
        All numbers (including target) will be positive integers.
        The solution set must not contain duplicate combinations.
        
        For example, given candidate set [2, 3, 6, 7] and target 7, A solution set is: [[7],[2,2,3]]
        """
        
