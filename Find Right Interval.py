# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    # bucket sort solution, O(n), beats 100%
    def findRightInterval(self, intervals):
        Max = float('-Inf')         # find the max start
        Min = float('Inf')          # find the min start
        length = len(intervals)
        
        for interval in intervals:
            Max = max(Max, interval.start)
            Min = min(Min, interval.start)
            
        Range = Max-Min+1
        
        bucket = [-1 for _ in xrange(Range)]        # store head index in corresponding position
        for i,interval in enumerate(intervals):
            bucket[interval.start-Min] = i
            
        res = [-1 for _ in xrange(length)]          # init a result list
        for i, interval in enumerate(intervals):# for each interval's end, find the closest next interval head in bucket if exist
            j = interval.end-Min                    
            
            while j<Range and bucket[j] == -1:
                j+=1
            
            if j<Range:
                res[i] = bucket[j]
        return res
            
            
        
        
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        
        
        # Given a set of intervals, for each of the interval i, 
        # check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, 
        # which can be called that j is on the "right" of i.
        # For any interval i, you need to store the minimum interval j's index, 
        # which means that the interval j has the minimum start point to build the "right" relationship for interval i. 
        # If the interval j doesn't exist, store -1 for the interval i. 
        # Finally, you need output the stored value of each interval as an array.
