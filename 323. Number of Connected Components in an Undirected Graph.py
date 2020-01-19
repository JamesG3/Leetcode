class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [set() for _ in range(n)]
        
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
            
        visted = set()
        count = 0
        
        for i in range(n):
            if i in visted:
                continue
                
            dfs = [i]
            count += 1
            while dfs:
                tmp_dfs = []
                for node in dfs:
                    visted.add(node)
                    for nei in graph[node]:
                        if nei not in visted:
                            tmp_dfs.append(nei)
                dfs = tmp_dfs
        return count
                    
'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Solution: DFS
Time: O(n)
'''        
            
        
