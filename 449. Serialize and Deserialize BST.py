# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        return ' '.join(self.postorder(root))
    
    def postorder(self, node):
        if not node:
            return []
        
        right = self.postorder(node.right)
        left = self.postorder(node.left)
        
        # post order traversal, make sure the last node is the root of current subtree
        return right + left + [str(node.val)]
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """ 
        def helper(lower, upper):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
        
            val = data.pop()
            node = TreeNode(val)
            
            # reverse order to deserialize the BST, left first, the right
            node.left = helper(lower, val)
            node.right = helper(val, upper)
            
            return node
        
        # for empty string of searialized BST
        if not data:
            return None
        
        data = [int(_) for _ in data.split(' ')]
        return helper(-float('inf'), float('inf'))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


Solution: Tree traversal, BST, post order traversal
Time: O(n)
Space: O(n)
'''
