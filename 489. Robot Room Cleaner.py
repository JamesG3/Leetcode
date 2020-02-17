# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.robot = robot
        self.dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.visted = set()
        self.backtrack()
    
    # turn back one step and keep the same direction
    def back(self):
        self.robot.turnRight()
        self.robot.turnRight()
        self.robot.move()
        self.robot.turnRight()
        self.robot.turnRight()
        
    def backtrack(self, cur_cell = (0, 0), d_i = 0):
        self.visted.add(cur_cell)
        self.robot.clean()
        
        # change a direction once a time (start with going straight)
        for i in range(4):
            new_d_i = (d_i + i) % 4
            new_y, new_x = self.dirs[new_d_i]
            new_cell = (cur_cell[0] + new_y, cur_cell[1] + new_x)
            
            # backtracking, back to this position after each DFS, change a direction to do another DFS
            if new_cell not in self.visted and self.robot.move():
                self.backtrack(new_cell, new_d_i)
                self.back()
            
            # if direction changes, turn the robot
            self.robot.turnLeft()
        
'''
Given a robot cleaner in a room modeled as a grid.
Each cell in the grid can be empty or blocked.
The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.
When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.
Design an algorithm to clean the entire room using only the 4 given APIs shown below.

Solution: Backtracking, DFS, Hashtable
Time: O(4**(n)), where n is the number of cells need to be cleaned
Space: O(n)
'''
        
