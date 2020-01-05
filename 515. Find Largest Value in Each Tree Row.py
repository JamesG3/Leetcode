# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        
        if not root:
            return res
        
        row = [root]
        while row:
            tmp_row = []
            cur_max = -float('inf')
            for node in row:
                cur_max = max(cur_max, node.val)
                if node.left:
                    tmp_row.append(node.left)
                if node.right:
                    tmp_row.append(node.right)
                
            res.append(cur_max)
            row = tmp_row
            
        return res
                    
'''
You need to find the largest value in each row of a binary tree.

Solution: Level tree traverse
Space, Time: O(n)
'''        



