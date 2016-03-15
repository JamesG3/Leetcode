class Solution(object):
    def moveZeroes(self, nums):            #faster version
        i = 0
        zero = 0
        n = len(nums)
        while i+zero < n:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                zero += 1
            else:
                i += 1
        
        """
class Solution(object):                  #shorter version
    def moveZeroes(self, nums):
        for n in nums:
            if(n==0):
                nums.remove(0)
                nums.append(0)
        """
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
