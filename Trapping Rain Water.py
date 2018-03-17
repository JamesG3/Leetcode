class Solution(object):
    def trap(self, height):
        l, r = 0, len(height)-1
        lmax = rmax = 0
        res = 0
        
        while l < r:
            if height[l] < height[r]:
                if lmax < height[l]:
                    lmax = height[l]
                else:
                    res += lmax-height[l]
                l+=1
            else:
                if rmax < height[r]:
                    rmax = height[r]
                else:
                    res += rmax - height[r]
                r-=1
        return res
            
        
        
        """
        :type height: List[int]
        :rtype: int
        """
        
        
        # Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
        # For example, 
        # Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
