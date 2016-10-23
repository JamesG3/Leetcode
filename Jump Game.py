class Solution(object):
    def canJump(self, nums):
        move=1                    #move the first step
        for n in nums[:-1]:
            move-=1               #minus 1 for every step move
            if move==0 and n==0:
                return False
            else:                 #always choose the larger one (the step remain and new maximum jump length)
                move=max(move,n)
        return True


        """
        :type nums: List[int]
        :rtype: bool

        Given an array of non-negative integers, you are initially positioned at the first index of the array.
        Each element in the array represents your maximum jump length at that position.
        Determine if you are able to reach the last index.
        
        A = [2,3,1,1,4], return true.
        A = [3,2,1,0,4], return false.
        """
        
