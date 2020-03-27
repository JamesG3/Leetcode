class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        self.maze = maze
        self.destination = destination
        if not maze or not len(maze[0]):
            return False
        
        self.height = len(maze)
        self.width = len(maze[0])
        self.visted = set()
        self.found = False
        
        bfs = [start]
        while bfs:
            tmp_bfs = []
            for x, y in bfs:
                tmp_bfs += self.find_nxt_neis(x, y)
                if self.found:
                    return True
            bfs = tmp_bfs
        return self.found
    
             
    def find_nxt_neis(self, x, y):
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = []
        if (x, y) in self.visted:
            return res
        
        if [x, y] == self.destination:
            self.found = True
            return res
        
        self.visted.add((x, y))
        for i, j in dirs:
            new_x, new_y = x, y
            while 0 <= new_x < self.height and 0 <= new_y < self.width and self.maze[new_x][new_y] == 0:
                new_x, new_y = new_x + i, new_y + j
            if (new_x, new_y) not in self.visted:
                res.append([new_x - i, new_y - j])
        return res
    
'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Solution: conditional BFS, hash table, graph traverse
Time: O(mn)
Space: O(mn)
'''
