class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = sorted(timePoints)
        min_min = float('inf')
        for i in range(1, len(timePoints)):
            h_1, m_1 = timePoints[i-1].split(':')
            h_2, m_2 = timePoints[i].split(':')
            h_diff = int(h_2) - int(h_1)
            
            if h_diff == 0:
                min_diff = int(m_2) - int(m_1)
            else:
                min_diff = int(m_2) + (60-int(m_1)) + (h_diff-1) * 60
                
            min_min = min(min_min, min_diff)
            
        h_1, m_1 = timePoints[-1].split(':')
        h_2, m_2 = timePoints[0].split(':')
        h_diff = int(h_2) + (24 - int(h_1))
        
        min_diff = (h_diff - 1) * 60 + int(m_2) + (60 - int(m_1))
        min_min = min(min_min, min_diff)
        
        return min_min
    
'''
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Solution: Sort and traverse, compare each pair of neighbors
Time: O(nlogn)
Space: extra O(1)
'''    
        
