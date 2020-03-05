# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.subtrees = {}
        self.cnter = {}
        self.ans = []
        self.uid = 0
        self.helper(root)
        return self.ans
        
    def helper(self, node):
        if not node:
            return
        
        k = (node.val, self.helper(node.left), self.helper(node.right))
        if k not in self.subtrees:
            self.subtrees[k] = self.uid
            self.cnter[self.uid] = 1
            self.uid += 1
            
        else:
            self.cnter[self.subtrees[k]] += 1
            if self.cnter[self.subtrees[k]] == 2:
                self.ans.append(node)
            
        return k
            
'''
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with same node values.

Solution: DFS, tree traverse
Time: O(n)
Space: O(n)
'''
