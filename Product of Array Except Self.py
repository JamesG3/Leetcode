class Solution(object):
    def productExceptSelf(self, nums):
        
        if nums.count(0) >= 2:
            for index in range(0,len(nums)):
                nums[index]=0
            return nums
            
        elif nums.count(0) == 1:
            
            if len(nums)==1:
                return nums
            product=1
            for index in range(0,len(nums)):
                if nums[index] != 0:
                    product *= nums[index]
            for index in range(0,len(nums)):
                if nums[index] == 0:
                    nums[index]=product
                else:
                    nums[index]=0
            return nums
            
        else:
            product=1
            for index in range(0,len(nums)):
                product*=nums[index]
            for index in range(0,len(nums)):
                nums[index] = product/nums[index]
            return nums
            
            
            
        """
        :type nums: List[int]
        :rtype: List[int]
        
        Given an array of n integers where n > 1, nums, 
        return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
        """
        
