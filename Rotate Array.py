class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        if k!=0:
            tem=nums[-k:]               #rotate part of nums
            nums[-len(nums)+k:] = nums[:len(nums)-k]        #in-place replace elements in nums
            nums[:k] = tem              #in-place replace the rotate part
        
        
      #Rotate an array of n elements to the right by k steps.
      #For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
        

"""
    #TLE solution (usign O(1) extra space)
    def rotate(self, nums, k):
        
        k=k%len(nums)
        while k != 0:
            k-=1
            tem=nums[-1]
            for counter in xrange(len(nums)-1,-1,-1):
                nums[counter]=nums[counter-1]
            nums[0]=tem
            
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
"""
        
        
