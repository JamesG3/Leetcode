class Solution:
    def nextPermutation(self, nums):
        
        length = len(nums)
        i = length - 1
        if length <= 1:
            return
        
        currmin = float('Inf')
        while i > 0:
            if nums[i] <= nums[i-1]:
                i -= 1
            else:
                i -= 1
                break
        if i==0 and nums[i] >= nums[i+1]:
            nums[:] = nums[::-1]
            return
        
        else:
            for j in range(i, length):
                if nums[j] > nums[i]:
                    currmin = min(currmin, nums[j])
            for j in range(length-1, i-1, -1):
                if nums[j] == currmin:
                    nums[i], nums[j] = nums[j], nums[i]
            
            nums[i+1:] = nums[i+1:][::-1]
            return
        
        
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
        # If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
        # The replacement must be in-place, do not allocate extra memory.
        
