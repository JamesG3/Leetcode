# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        cur_level = [root]
        left_most = None
        
        while cur_level:
            left_most = cur_level[0].val
            tmp_level = []
            for node in cur_level:
                if node.left:
                    tmp_level.append(node.left)
                if node.right:
                    tmp_level.append(node.right)
            cur_level = tmp_level
            
        return left_most
                    
        
'''
Given a binary tree, find the leftmost value in the last row of the tree.

Solution: BFS, level traverse
Time, Space: O(n)
'''    
        
        
    
