class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_res = 0
        succ_cnt = 0
        # remove head
        p1, p2 = 0, len(seats)-1
        while seats[p1] == 0:
            succ_cnt += 1
            p1 += 1
        max_res = max(max_res, succ_cnt)
        succ_cnt = 0
        
        # remove tail
        while seats[p2] == 0:
            succ_cnt += 1
            p2 -= 1
        max_res = max(max_res, succ_cnt)
        succ_cnt = 0
                    
        # traverse the rest
        for i, n in enumerate(seats[p1:p2+1]):
            if n == 0:
                succ_cnt += 1
            
            if n == 1:
                max_res = max(max_res, (succ_cnt + 1) // 2)
                succ_cnt = 0
                
        return max_res


'''
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
There is at least one empty seat, and at least one person sitting.
Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
Return that maximum distance to closest person.

Solution: Traverse, edge case
Time: O(n)
'''


