# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        bfs = [root]
        res_levl, max_sum = 0, -float('inf')
        levl = 0
        
        while bfs:
            cur_sum = 0
            levl += 1
            tmp_bfs = []
            for node in bfs:
                cur_sum += node.val
                if node.left:
                    tmp_bfs.append(node.left)
                if node.right:
                    tmp_bfs.append(node.right)
            if cur_sum > max_sum:
                max_sum = cur_sum
                res_levl = levl
            
            bfs = tmp_bfs
                
        return res_levl
    
    
'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

Solution: BFS, level traverse
Time, Space: O(n)
'''
            
            
        
        
