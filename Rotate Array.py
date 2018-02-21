class Solution(object):
    def rotate(self, nums, k):
        
        # solution 1
#         k = k % len(nums)
#         if k == 0:
#             return
            
#         nums[:] = nums[-k:] + nums[:len(nums)-k]
        
        
        # solution 2: rotate
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:] = nums[:k][::-1] + nums[k:][::-1]
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        
        # Rotate an array of n elements to the right by k steps.
        # For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
        # Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
