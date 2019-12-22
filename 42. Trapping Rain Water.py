class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = 0
        rmax = 0
        res = 0
        
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                if height[l] < lmax:
                    res += lmax - height[l]
                else:
                    lmax = height[l]
                l += 1
                    
            else:
                if height[r] < rmax:
                    res += rmax - height[r]
                else:
                    rmax = height[r]
                r -= 1
                
        return res
            
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Solution: Two pointers, monitoring & updating the temp_left_max and temp_right_max
Time, Space: O(n)
'''
