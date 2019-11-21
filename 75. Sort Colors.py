class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        h, t = 0, len(nums) - 1
        i = 0
        while i <= t:
            if nums[i] == 0:
                nums[h], nums[i] = nums[i], nums[h]
                h += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[t] = nums[t], nums[i]
                t -= 1
            else:
                i += 1
                
        return nums
            
'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.
Solution: Two pointers, one pass
O(n)
'''
