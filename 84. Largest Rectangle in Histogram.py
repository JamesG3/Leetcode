class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [[-1, -1]]
        max_area = 0
        
        for i, n in enumerate(heights):
            if n >= stack[-1][1]:
                stack.append([i, n])
                continue
                
            while n < stack[-1][1]:
                j, m = stack.pop()
                # calculate each rectangle's area until only one element in stack
                max_area = max(max_area, m * (i - 1 - stack[-1][0]))
                
            stack.append([i, n])
        
        while stack[-1][1] != -1:
            j, m = stack.pop()
            # the end of list, so we should calculate the length * min_val as the last area
            max_area = max(max_area, m * (i - stack[-1][0]))
            
        return max_area
    
    
'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Solution: Stack
Time & Space: O(n)
'''
