# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda x:x.start)
        ans = []
        
        for i in intervals:
            if not ans or i.start > ans[-1].end:
                ans.append(i)
            else:
                ans[-1].end = max(ans[-1].end, i.end)
                
        return ans
                    
        
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        # Given a collection of intervals, merge all overlapping intervals.
