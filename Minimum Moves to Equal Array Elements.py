"""
class Solution(object):                                   # brute force solution
    def minMoves(self, nums):
        step=0
        while nums.count(nums[0])!=len(nums):
            temmax=max(nums)
            temmin=min(nums)
            temstep=temmax-temmin
            
            
            if nums.count(temmax)>1:
                step+=1
                count=1
                for n in range(0,len(nums)):
                    if nums[n] != temmax:
                        nums[n]+=1
                    else:
                        count-=1
                        if count<0:
                            nums[n]+=1
                    continue
                    
            else:
                step+=temstep
                for n in range(0,len(nums)):
                    if nums[n]!=temmax:
                        nums[n]+=temstep
        return step
            
        """
        :type nums: List[int]
        :rtype: int
        """
"""
