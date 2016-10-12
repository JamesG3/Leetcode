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
        
    
    def find(self, can, tar, index, res, tem):
        if tar==0:
            res.append(tem)
            return
        if tar < 0:
            return
        else:
            for m in range(index,len(can)):
                self.find(can, tar-can[m], m, res, tem+[can[m]])
        
        """
        :type candidates: List[int]a
        :type target: int
        :rtype: List[List[int]]
        """
        
