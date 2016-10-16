class Solution(object):
    def sortColors(self, nums):
        for n in range (1,len(nums)):
		    key = nums[n]
		    m = n-1
		    while m>=0 and nums[m]>key:
		        nums[m+1],nums[m]=nums[m],nums
		        m-=1
		        nums[m+1]=key
            
