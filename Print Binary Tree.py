# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        Depth = self.getDepth(root)
        global res
        res = []
        for i in xrange(Depth):             # initialize the answer array
            res.append([""]*(2**Depth-1))
        self.helper(root, 0, 0, 2**Depth-1)
        return res
            
        
    def getDepth(self, root):
        if root is None:
            return 0
        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1
        
    def helper(self, root, depth, head, tail):
        global res
        if root is None:
            return
        res[depth][(head+tail)/2] = str(root.val)               # for each level, replace the corresponding mid position
        self.helper(root.left, depth+1, head, (head+tail)/2)    # update the head and tail for next level
        self.helper(root.right, depth+1, (head+tail)/2+1, tail)
        return
        
        
    
    
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        # print binary tree using 2D array.
