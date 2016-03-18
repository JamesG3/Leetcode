class Solution(object):
    def twoSum(self, nums, target):
        tem = {}
        for i,num in enumerate(nums):           #save every number in tem for the following searching action 
            if num not in tem:
                tem[target-num]=i
            else:
                return [min(i,tem[num]),max(i,tem[num])]    #picking up number according to the value


        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
