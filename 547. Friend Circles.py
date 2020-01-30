class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        counter = 0
        visted = set()
        length = len(M)
        
        for i, row in enumerate(M):
            for k, n in enumerate(row[i:]):
                j = i+k
                if n == 0 or (i, j) in visted:
                    continue
                    
                dfs = [[i, j]]
                counter += 1
                while dfs:
                    f_i, f_j = dfs.pop()
                    visted.add((f_i, f_j))
                    for _ in range(length):
                        if (f_i, _) not in visted and M[f_i][_]:
                            visted.add((f_i, _))
                            dfs.append([f_i, _])
                        if (_, f_j) not in visted and M[_][f_j]:
                            visted.add((_, f_j))
                            dfs.append([_, f_j])      
        
        return counter
                            
'''
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Solution: DFS, traverse half of the friend matrix
Time: O(n**2)
Space: O(n)
'''               
                    
         
