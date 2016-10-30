class Solution(object):
    def productExceptSelf(self, nums):
        #without divsion
        res=[]
        product=1                               #calculate product from left to right
        for n in range(0,len(nums)):
            res.append(product)
            product *= nums[n]
            
        product = 1
        for n in range(len(nums)-1, -1, -1):        #calculate product from right to left
            res[n] *= product                   #with one digit shift amount
            product *= nums[n]
        
        return res
        
        
        
        """
        #version of using division
        
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
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
