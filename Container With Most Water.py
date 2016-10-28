class Solution(object):
    def maxArea(self, height):
        area=min(height[0],height[-1])*(len(height)-1)        #initialize the area with the first bar and the last bar
        head=0
        tail=len(height)-1
        while head != tail:                                   #when head and tail are not met
            if height[head]<=height[tail]:                    #always choose the larger bar
                head+=1
            elif height[tail]<height[head]:
                tail-=1
            area=max(area, min(height[head],height[tail])*(tail-head))    #then check if the area gets larger
            
        return area
        """
        :type height: List[int]
        :rtype: int
        
        Given n non-negative integers a1, a2, ..., an, 
        where each represents a point at coordinate (i, ai). 
        n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
        Find two lines, which together with x-axis forms a container, such that the container contains the most water.
        
        **********
        We need to find the largest area of this coordinate, 
        and it is ok if there is any higher bar between the two bars we've chose.
        """
        
