class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        ns, ne = newInterval
        p, length = 0, len(intervals)
        
        # deal with the intervals until overlap happens (include the overlapped interval)
        while p < length and ns > intervals[p][0]:
            res.append(intervals[p])
            p += 1
            
        # merge the new interval with the first overlapped interval
        if not res or res[-1][-1] < ns:
            res.append([ns, ne])
        else:
            res[-1][-1] = max(res[-1][-1], ne)
            
        # deal with the rest of intervals after first overlapped interval
        while p < length:
            s, e = intervals[p]
            p += 1
            # overlapping ends starts from this condition
            if res[-1][-1] < s:
                res.append([s, e])
            # if overlap, merge the current interval with the last interval in res
            else:
                res[-1][-1] = max(res[-1][-1], e)
        return res

    '''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Solution: Greedy
Time, Space: O(n)
'''
