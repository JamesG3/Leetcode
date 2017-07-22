# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        if root is None:
            return []
        
        res = []
        Stack = [root]
        
        while Stack:                        # loop until there is no more level
            Sum = 0
            count = 0
            temStack = []
            while Stack:                        # traverse all node from the current level
                current = Stack.pop()
                if current.left:                # append next level's node to temStack
                    temStack.append(current.left)
                if current.right:
                    temStack.append(current.right)
                count += 1
                Sum += current.val              # calculate the average for the current level
            res.append(1.0*Sum/count)
            Stack = temStack                    # move to the next level
            
        return res
        
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
