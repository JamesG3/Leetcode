import random                                           #a simple but time consuming solution
import math
class Solution(object):
    def permute(self, nums):
    res = []
    while len(res) < math.factorial(len(nums)):
        random.shuffle(nums)
        if nums not in res:
            res.append(nums[:])
    return res
    #def permute(self, nums):
    #    num=nums[:]
    #    tem=num[:]
    #    res=[num]
    #    length=len(res)
    #    while(len(res)<math.factorial (len(nums))):
    #        if(tem not in res):
    #            res.append(tem)
    #        else:
    #            random.shuffle(nums)
    #            tem=nums[:]
    #    return res
            
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
