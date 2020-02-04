# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.par = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # build parent links
        self.dfs_p(root, None)
        
        dfs = [target]
        res = []
        visted = set([target])
        for i in range(K):
            tmp_dfs = []
            for node in dfs:
                for nei in [node.par, node.left, node.right]:
                    if nei and nei not in visted:
                        visted.add(nei)
                        tmp_dfs.append(nei)
            dfs = tmp_dfs
        return [n.val for n in dfs]
                    

        
    def dfs_p(self, node, par):
        if not node:
            return
        node.par = par
        self.dfs_p(node.left, node)
        self.dfs_p(node.right, node)
            
'''
We are given a binary tree (with root node root), a target node, and an integer value K.
Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

Solution: BFS, graph, parent, Tree
Time, Space: O(n)
'''

