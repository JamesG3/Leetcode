from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnter = Counter(tasks)
        scheduled = 0
        total_time = 0
        
        while scheduled < len(tasks):
            # cool down time need to be n+1 because n is the gap intervals between two same tasks
            gap_cd = n+1
            
            # traverse the tasks from those with highest counts
            # most_common() funtion will return a list of [(item1, 10), (item2, 10), (item3, 9), ...] in descending order
            for task, cnt in cnter.most_common():
                # if cool down, we may start from the begninning
                if gap_cd == 0:
                    break
                # if reach the elements with 0 count, should start from the beginning (cuz rest of elements are all 0)
                if cnter[task] == 0:
                    break
                    
                gap_cd -= 1
                total_time += 1
                scheduled += 1
                cnter[task] -= 1
                
                if scheduled == len(tasks):
                    gap_cd = 0
                    break
            # after traversing all elements in cnter, if still needs time to cool down, add these to total_time
            total_time += gap_cd                
        
        return total_time
                
'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.
You need to return the least number of intervals the CPU will take to finish all the given tasks.

Solution: Hash table, priority queue, greedy
Time: O(n)
SpaceL O(26) -> O(1)
'''

        
