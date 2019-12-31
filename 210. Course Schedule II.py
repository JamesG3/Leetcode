class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.res = []
        self.pre_dic = {}
        self.c_status = {}              # 0: initial status, 1: waiting for other courses, 2: course can be taken now
        self.visted = set()
        self.valid_flag = True          # mark if loop detected - then it's impossible to finish all the courses
        
        for c, pre in prerequisites:
            if c not in self.pre_dic:
                self.pre_dic[c] = []
            self.pre_dic[c].append(pre)
            self.c_status[c] = 0
        
        
        # finish all courses without dependencies
        for c in range(numCourses):
            if c not in self.c_status:
                self.c_status[c] = 2
                self.res.append(c)
                
        for k,v in self.pre_dic.items():
            self.helper(k)
            if not self.valid_flag:
                return []
            
        return self.res
                
        
    def helper(self, c):
        if self.c_status[c] == 2:
            self.visted.add(c)
            return
        
        # loop detected, set flag to false
        if self.c_status[c] == 1:
            self.valid_flag = False
            return
        
        # waiting for all other courses finished
        self.c_status[c] = 1
        for pre in self.pre_dic[c]:
            self.helper(pre)
            if not self.valid_flag:
                return
        
        # finish all dependencies, update the status of this course
        self.c_status[c] = 2
        if c not in self.visted:
            self.visted.add(c)
            self.res.append(c)
        return
            
                
        
'''
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Solution: DFS, hashtable, recursive, state machine
Time, Space: O(n)
'''    
