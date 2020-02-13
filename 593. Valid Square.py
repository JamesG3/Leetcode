class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 or p2 == p3 or p3 == p4 or p4 == p1 or p3 == p1 or p2 == p4:
            return False
        
        edges = [
            self.get_dist(p1, p2),
            self.get_dist(p2, p3),
            self.get_dist(p3, p4),
            self.get_dist(p1, p4),
            self.get_dist(p2, p4),
            self.get_dist(p1, p3)
        ]
        edges.sort()
        return len(set(edges[:4])) == 1 == len(set(edges[4:])) and 2*edges[0] == edges[-1]
        
    def get_dist(self, pa, pb):
        return (pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2
    
'''
Given the coordinates of four points in 2D space, return whether the four points could construct a square.
The coordinate (x,y) of a point is represented by an integer array with two integers.

Solution: Math, special square feature, edge case
Time: O(n)
Space: O(1)
'''
