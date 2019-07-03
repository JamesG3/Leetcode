import math
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        Solution: sort
        Time: O(nlgn)
        Space: O(n)
        """
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
    
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)    
