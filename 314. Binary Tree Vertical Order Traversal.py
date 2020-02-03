# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.location = 0

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        self.min_mark = float('inf')
        self.max_mark = -float('inf')
        self.mark(root, 0)
        if not root:
            return []
        
        mark_range = self.max_mark - self.min_mark + 1
        res = [[] for i in range(mark_range)]
        bfs = [root]
        while bfs:
            tmp_bfs = []
            for node in bfs:
                i = node.location - self.min_mark
                res[i].append(node.val)
                if node.left:
                    tmp_bfs.append(node.left)
                if node.right:
                    tmp_bfs.append(node.right)
            bfs = tmp_bfs
        return res
        
        
    def mark(self, node, cur_mark):
        if not node:
            return
        
        node.location = cur_mark
        self.min_mark = min(self.min_mark, cur_mark)
        self.max_mark = max(self.max_mark, cur_mark)
        self.mark(node.left, cur_mark - 1)
        self.mark(node.right, cur_mark + 1)
        
'''
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

Solution: BFS, traverse and mark, Array, Tree
Time: O(n)
Space: O(n)
'''
