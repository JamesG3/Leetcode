class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        rec_dict = {}
        # sort the list with y as the key
        points = sorted(points, key = lambda x: x[1])
        # for each x, get it's sorted ys
        for x, y in points:
            if x not in rec_dict:
                rec_dict[x] = []
            rec_dict[x].append(y)
        
        edges = {}
        res = float('inf')
        for k in sorted(rec_dict):
            ys = rec_dict[k]
            # get all combination of y pair for each x
            for i, y in enumerate(ys):
                for j, y2 in enumerate(ys[:i]):
                    # always save the previous (closest) snapshot x of each distinct (y, y2) pair
                    if (y, y2) in edges:
                        res = min(res, abs(edges[(y, y2)] - k) * abs(y - y2))
                    edges[(y, y2)] = k
        return res if res != float('inf') else 0
                    
                
'''
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.
If there isn't any rectangle, return 0.

Solution: Greedy, Hashtable, math
Time: O(n^2)
Space: O(n)
'''
            
