# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        
        return self.generate(1, n)
    
    def generate(self, start, end):
        if start > end:
            return [None]
        
        all_trees = []
        for i in range(start, end+1):
            left_trees = self.generate(start, i-1)
            right_trees = self.generate(i+1, end)
            
            for l in left_trees:
                for r in right_trees:
                    cur_root = TreeNode(i)
                    cur_root.left = l
                    cur_root.right = r
                    all_trees.append(cur_root)
        return all_trees
    
    
'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Solution: DP, Recursive, calculate all subtrees, save them in DP, then append all combinations in each level's all_trees
'''
