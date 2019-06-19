class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        Time: O(nlogn)
        Space: O(n)
        """
        return sum([1 for x,y in zip(heights, sorted(heights)) if x!=y])
        
        
        
        
  # Students are asked to stand in non-decreasing order of heights for an annual photo.
  # Return the minimum number of students not standing in the right positions.  
  # (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)   
  
