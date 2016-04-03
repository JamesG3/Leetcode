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
        #Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
