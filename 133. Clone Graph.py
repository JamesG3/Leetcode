"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visted = {}
        
        res_node = self.helper(node)
        return res_node
        
        
    def helper(self, node):
        if node in self.visted:
            return self.visted[node]
        
        tmp_node = Node(node.val, [])
        # need to use hashmap to save the deep copied node, and use the orig node as the key.
        self.visted[node] = tmp_node
        for n in node.neighbors:
            nei_node = self.helper(n)
            tmp_node.neighbors.append(nei_node)
        return tmp_node

'''
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

Solution: Hashmap, Graph deep copy, DFS
Time, Space: O(n)
'''
        
