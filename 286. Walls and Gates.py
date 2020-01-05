class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        bfs = []
        visted = set()
        for i, row in enumerate(rooms):
            for j, n in enumerate(row):
                if n == 0:
                    bfs.append([i, j])
                    
        if not bfs:
            return rooms
    
        cur_dist = 0
        height = len(rooms)
        width = len(rooms[0])
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        while bfs:
            cur_dist += 1
            tmp_bfs = []
            for m, n in bfs:
                for dir_x, dir_y in dirs:
                    i, j = m + dir_x, n + dir_y
                    if (0 <= i < height) and (0 <= j < width) and (i, j) not in visted:
                        if rooms[i][j] == 2147483647:
                            rooms[i][j] = cur_dist
                            visted.add((i, j))
                            tmp_bfs.append([i, j])
            bfs = tmp_bfs
        return rooms
    
'''
You are given a m x n 2D grid initialized with these three possible values.
-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Solution: BFS
Time, Space: O(n)
'''
                            

