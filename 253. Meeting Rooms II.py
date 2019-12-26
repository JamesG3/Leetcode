class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        
        for s_time, e_time in sorted(intervals, key = lambda x: x[0]):
            room_i = 0
            min_time = float('inf')
            for i, room in enumerate(rooms):
                if 0 <= (s_time - room[-1]) < min_time:
                    min_time = (s_time - room[-1])
                    room_i = i
            if min_time == float('inf'):
                rooms.append([e_time])
            else:
                rooms[room_i].append(e_time)
                
        return len(rooms)
                    
'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Solution: Greedy, 
Time: O(nlogn)
Space: O(n)
'''
