class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        for i, interval in enumerate(sorted_intervals[1:]):
            if sorted_intervals[i][-1] > interval[0]:
                return False    
        return True
    
    
'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Solution: Sort
Time: O(nlogn)
Space: O(n)
'''
