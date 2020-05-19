# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        return [_ for _ in self.helper([root])]
        
        
    def helper(self, nodes):
        if not nodes:
            return
        
        nxt_level = []
        cur_sum = []
        for node in nodes:
            cur_sum.append(node.val)
            if node.left:
                nxt_level.append(node.left)
            if node.right:
                nxt_level.append(node.right)
        yield sum(cur_sum) / len(cur_sum)
        yield from self.helper(nxt_level)
        
'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Solution: recursive level traversal, BFS
Time, Space: O(n)
'''
