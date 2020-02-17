# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        forest = []
        to_delete = set(to_delete)
        
        dfs = [[root, None]]
        while dfs:
            node, parent = dfs.pop()
            if node.val in to_delete:
                if node.left:
                    dfs.append([node.left, None])
                if node.right:
                    dfs.append([node.right, None])
            else:
                if node.left:
                    dfs.append([node.left, node])
                    if node.left.val in to_delete:
                        node.left = None
                if node.right:
                    dfs.append([node.right, node])
                    if node.right.val in to_delete:
                        node.right = None
                if not parent or parent.val in to_delete:
                    forest.append(node)
        return forest

'''
Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest.  You may return the result in any order.

Solution: DFS, Stack, iterative tree traversal
Time, Space: O(n)
'''
