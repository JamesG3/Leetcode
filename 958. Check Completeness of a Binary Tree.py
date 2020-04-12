# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        end_flag = False
        bfs = [root]
        
        while bfs:
            tmp_bfs = []
            for node in bfs:
                left_node = node.left if node.left else None
                right_node = node.right if node.right else None
                
                if end_flag and (left_node or right_node):
                    return False
                
                if not left_node and not right_node:
                    end_flag = True
                    
                elif not left_node and right_node:
                    return False
                
                elif left_node and not right_node:
                    end_flag = True
                    
                if left_node:                
                    tmp_bfs.append(left_node)
                if right_node:
                    tmp_bfs.append(right_node)
            
            bfs = tmp_bfs
            
        return True
                    
'''
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Solution: BFS, tree level traversal, once end_flag is on, there shouldn't be more nodes found
Time: O(n)
Space: O(n)
'''          
                    
        
