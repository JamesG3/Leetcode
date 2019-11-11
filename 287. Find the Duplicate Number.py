class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the intersection point of the two runners.
        slw, fst = nums[0], nums[0]
        while True:
            slw = nums[slw]
            fst = nums[nums[fst]]
            if slw == fst:
                break
        
        # Find the "entrance" to the cycle.
        p1, p2 = nums[0], slw
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
            
        return p1
        
'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
'''        
