class Solution(object):
    def twoSum(self, nums, target):
        tem = {}
        for i,num in enumerate(nums):           #save every number in tem for the following searching action 
            if num not in tem:
                tem[target-num]=i
            else:
                return [min(i,tem[num]),max(i,tem[num])]    #picking up number according to the value

            
            
class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        i = 0
        for n in nums:
            if target-n in dic:
                return [dic[target-n][0] ,i]
            
            dic[n] = [i, target-n]
            i += 1
         
        
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution.
