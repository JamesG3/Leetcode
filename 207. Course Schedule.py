class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = {}
        self.status = [0 for i in range(numCourses)]
        for i,j in prerequisites:
            if j not in self.graph:
                self.graph[j] = set()
            self.graph[j].add(i)
            
        for node in self.graph:
            if self.status[node] == 0:
                if not self.dfs(node):
                    return False
        return True
        
        
    def dfs(self, node):
        self.status[node] = 1
        if node in self.graph:
            for n in self.graph[node]:
                if self.status[n] == 0:
                    if not self.dfs(n):
                        return False
                # non-complete status, loop is detected
                if self.status[n] == 1:
                    return False
        # complete status
        self.status[node] = 2
        return True
            
'''
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Solution: graph loop detection
Time: O(V+E)
Space: O(V+E) 
'''      

