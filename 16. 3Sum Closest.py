from collections import Counter

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        O(n^2), traverse one element, use two pointer to traverse the rest
        Skip dup nums
        """
         
        nums.sort()
        length = len(nums)
        res = float('inf')
        
        for i1 in xrange(0, length - 2):
            if i1 > 0 and nums[i1] == nums[i1 - 1]:
                continue
            
            left, right = i1 + 1, length - 1
            
            while left < right:
                tmp_sum = nums[i1] + nums[left] + nums[right]
                if abs(tmp_sum - target) < abs(res - target):
                    res = tmp_sum
                if res == target:
                    return target
                
                elif tmp_sum < target:
                    left += 1
                else:
                    right -= 1
        return res
    
    
  
        # Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. 
        # You may assume that each input would have exactly one solution.
        
        # Given array nums = [-1, 2, 1, -4], and target = 1.
        # The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
                
            
            
            
            
                    
                
                    
                    
        
        
        
        
        
        
        
