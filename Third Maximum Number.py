class Solution(object):
    def thirdMax(self, nums):
        nums.sort()                     #sort the list
        max=nums[-1]
        counter=2                       #use a counter to mark the second maximum number
        
        for i in range(len(nums)-1,-1,-1):  #read from the largest number
            if nums[i] < max:
                counter-=1
                max=nums[i]
            if counter == 0:
                return max
        return nums[-1]
        
        """
        :type nums: List[int]
        :rtype: int
        
        Given a non-empty array of integers, return the third maximum number in this array. 
        If it does not exist, return the maximum number. The time complexity must be in O(n).
        """
