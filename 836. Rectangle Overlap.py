class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return not any([
            x1 >= x4,
            x2 <= x3,
            y1 >= y4,
            y2 <= y3,
        ])
    
'''
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.
Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.
Given two (axis-aligned) rectangles, return whether they overlap.

Solution: Check corner range (compare left corner with right corner, make sure there is no overlap)
Time, Space: O(1)
'''
        
