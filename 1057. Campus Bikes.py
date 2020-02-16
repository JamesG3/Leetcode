class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        assign = []
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                w_i, w_j = w
                b_i, b_j = b
                dist = abs(w_i - b_i) + abs(w_j - b_j)
                assign.append([i, j, dist])
        assign = sorted(assign, key = lambda x: (x[-1], x[0]))
        mapping = {}
        assigned = set()
        for i, j, dist in assign:
            if i in mapping or j in assigned:
                continue
            mapping[i] = j
            assigned.add(j)
        
        return [mapping[i] for i in range(len(workers))]
            
'''
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.
Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.
The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.

Solution: Hashtable, Hashset
Time, Space: O(n*m)
'''        
            
