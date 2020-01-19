class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(n)]
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
            
        leaves = [_ for _ in range(n) if len(graph[_]) <= 1]
        ans = leaves
        while leaves:
            tmp_leaves = []
            for leaf in leaves:
                # if there is only one leaf left, no edge at all
                if not graph[leaf]:
                    return leaves
                
                nei = graph[leaf].pop()
                # cut leaf from the only neighbor
                graph[nei].remove(leaf)
                if len(graph[nei]) == 1:
                    tmp_leaves.append(nei)
                    
            ans, leaves = leaves, tmp_leaves
            
        return ans
            
'''
For an undirected graph with tree characteristics, we can choose any node as the root. 
The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). 
Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Solution: Graph, Strip & Cut leaves from the outside, level by level, until all the nodes left are leaves (they are in the certer of the graph)
Time: O(n)
'''
