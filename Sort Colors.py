class Solution(object):
    def sortColors(self, nums):
        for n in range (1,len(nums)):
		key = nums[n]
		m = n-1
		while m>=0 and nums[m]>key:
			nums[m+1],nums[m]=nums[m],nums
		        m-=1
		        nums[m+1]=key
			
			
			
			
#using insertion sort
            
#Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

#Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
