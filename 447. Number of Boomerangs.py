class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        length = len(points)
        res = 0
        
        for i in range(length):
            dic = {}
            for j in range(length):
                if i == j:
                    continue
                dist = self.get_dist(points[i], points[j])
                if dist not in dic:
                    dic[dist] = 0
                dic[dist] += 1
                
            for v in dic.values():
                res += v * (v - 1)  
        return res
                
    def get_dist(self, pointA, pointB):
        return (pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2
        
        
'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Solution: hashtable, traverse every pair of points, calculate the distance, add the count to res
            use hashtable to store count of same distance for each point
            then use v * (v - 1) to calculate the number of combinations
Space: O(n)
Time: O(n^2)
'''
