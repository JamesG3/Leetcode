class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for n in nums:
                if(n>target):
                    return nums.index(n)
            if(target<nums[0]):
                return 0
            elif(target>nums[-1]):
                return len(nums)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
