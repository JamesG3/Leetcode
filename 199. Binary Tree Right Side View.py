# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        bfs = [root]
        res = []
        
        if not root:
            return res
        
        while bfs:
            tmp_bfs = []
            res.append(bfs[-1].val)
            
            for node in bfs:
                if node.left:
                    tmp_bfs.append(node.left)
                if node.right:
                    tmp_bfs.append(node.right)
            bfs = tmp_bfs
        return res
                    
'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Solution: BFS, level, traversal
Time: O(n)
Space: O(n)
'''
