class Solution(object):
    def minMoves(self, nums):
        
        step=0
        nums.sort()
        for n in range(len(nums)-1,-1,-1):
            if nums[n] == nums[0]:
                break
            else:
                step+=nums[n]-nums[0]
            
        return step
    
       #return sum(nums) - len(nums)*min(nums)
       #onelinesolution       
        """
        :type nums: List[int]
        :rtype: int
        
        
        Given a non-empty integer array of size n, 
        find the minimum number of moves required to make all array elements equal, 
        where a move is incrementing n - 1 elements by 1.
        """

        
"""
# brute force solution

class Solution(object):
    def minMoves(self, nums):
        
        step=0
        while nums.count(nums[0])!=len(nums):
            temmax=max(nums)
            temmin=min(nums)
            temstep=temmax-temmin
            step+=temstep
            count=1
            point=nums.index(temmax)
            for n in range(0,len(nums)):
                if nums[n]!=temmax:
                    nums[n]+=temstep
                else:
                    count-=1
                    if count<0:
                        nums[n]+=temstep
            
        return step
            
        """
