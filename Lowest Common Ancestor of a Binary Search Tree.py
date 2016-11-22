# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val>q.val:             #put p and q in order p<q
            return self.lowestCommonAncestor(root,q,p)
            
        while not p.val<=root.val<=q.val: #find the node which satisfy p.val<=root.val<=q.val (including the root itself is p or q)
            if p.val<root.val:
                root=root.left
            elif p.val>root.val:
                root=root.right

        return root
        """
        using the property of BST
        
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
