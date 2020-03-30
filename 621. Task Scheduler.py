# counter solution (using most_common())
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

# heap solution
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnter = {}
        for task in tasks:
            cnter[task] = cnter.get(task, 0) + 1
        
        heap = [(-cnt, task) for task, cnt in cnter.items()]
        heapq.heapify(heap)
        stack = []
        
        scheduled = 0
        total_time = 0
        
        while scheduled < len(tasks):
            cd_time = n + 1
            while heap:
                if cd_time == 0:
                    break
                
                cnt, task = heapq.heappop(heap)
                cnt += 1
                stack.append((cnt, task))
                total_time += 1
                cd_time -= 1
                scheduled += 1
                
                if scheduled == len(tasks):
                    cd_time = 0
                    break
                
            total_time += cd_time
            
            while stack:
                cnt, task = stack.pop()
                if cnt == 0:
                    continue
                heapq.heappush(heap, (cnt, task))
            
        return total_time
'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.
You need to return the least number of intervals the CPU will take to finish all the given tasks.

Solution: Hash table, priority queue, greedy
Time: O(n)
SpaceL O(26) -> O(1)
'''

        
