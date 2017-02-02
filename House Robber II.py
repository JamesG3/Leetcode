class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:      #edge case
            return nums[0]
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))       #delete the first element/ delete the last element
                                                                    #return the larger result
        
    def rob1(self, nums):
        current = 0
        last = 0
        
        for n in nums:
            last, current = current, max(last+n, current)
            
        return current
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        
        #After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
        #Meanwhile, the security system for these houses remain the same as for those in the previous street.
