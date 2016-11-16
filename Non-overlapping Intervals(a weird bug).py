# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if len(intervals)==0:
            return 0
        
        count=0
        intervals.sort()
        temend=intervals[0].end
        
        for n in intervals[1:]:
            if n.start>=temend:
                temend=n.end
            else:               #erase
                count+=1
                temend=min(temend,n.end)
        return count
            
        
        """
        Given a collection of intervals, 
        find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
        You may assume the interval's end point is always bigger than its start point.
        Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
        
        :type intervals: List[Interval]
        :rtype: int
        """
        
