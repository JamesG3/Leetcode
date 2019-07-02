# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Solution: level traverse (BFS)
        Time: O(n)
        Space: O(n)
        """
        q = []
        res = []
        
        if not root:
            return res
        
        res.append(root.val)
        q.append(root)
        
        while True:
            tmp = []
            for node in q:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if not tmp:
                break
                
            res.append(tmp[-1].val)
            q = tmp
            
        return res
                    
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.    
        
