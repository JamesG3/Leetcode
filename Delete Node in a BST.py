# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        Del=self.Search(root,key)       #first, searching where the node is 
        if Del==None:                   #if the target node isn't in the tree, then return the original tree without modify
            return root
            
        if Del==root:       #if the target node is the root, i build a function for rootdeletion, make the logic more clear
            return self.rootdeletion(root)
            
                            #if the target node is in the tree, execute the code below:
        parent=self.parent(root, key)   #find the parent of Del, will be used for transplanting and locating node.

        
        if Del.right == None and Del.left==None:    #the 1st situation of BST deletion: no children
            if parent.left==Del:
                parent.left=None
            else:
                parent.right=None
                
        elif Del.right != None and Del.left == None:    #the 2nd situation of BST deletion: only right child
            if parent.left==Del:
                parent.left=Del.right
            else:
                parent.right=Del.right
                
        elif Del.left != None and Del.right == None:    #the 3rd situation of BST deletion: only left child
            if parent.left==Del:
                parent.left=Del.left
            else:
                parent.right=Del.left
                
        else:                               #the 4th situation of BST deletion: two children

            min=self.Min(Del.right)         #find the Min of Del's right subtree
            if min==Del.right:              #if the Min is right child of Del
                if parent.left==Del:        #tansplant
                    parent.left=min
                    min.left=Del.left
                else:                       
                    parent.right=min
                    min.left=Del.left
                
                return root

            minparent=self.parent(root, min.val)
                                        # when min is not the right child of Del, execute the code below:
            if min.right==None: #when the Minimum node doesn't have right child, then delete the connection and do transplant
                minparent.left=None
                        
                        #when the Minimum node has right child, fist take out the Minimum node, transplant the Min.right subtree, and transplant Min node:
            else:
                if minparent.left==min:
                    minparent.left=min.right
                else:
                    min.parent.right=min.right
            
            if parent.left==Del:    #do the rest of transplant
                parent.left=min
            else:
                parent.right=min
                    
            if Del.right != None:
                min.right=Del.right
            if Del.left != None:
                min.left=Del.left
                
        return root
        
        
        
    def Min(self, root):            #in this treenodeDeletion, we use successor to transplant with Del
        res=root                    #so we need to find the Minimum of a subtree
        while res.left!=None:
            res=res.left
        return res
    
    def Search(self, root, key):        #this function is used for searching the node whose key is "key"
        res=root
        while True:
            if res == None or res.val == key:   #if "key" is not in the tree, return None
                break
            elif res.val<key:
                res=res.right
            else:
                res=res.left
        return res
            
    def parent(self, root, k):          #this funciton is used for finding parent
        parent=root
        while True:
            if parent.val<k:
                if parent.right.val==k:
                    break
                parent=parent.right
            elif parent.val>k:
                if parent.left.val==k:
                    break
                parent=parent.left
            else:
                break
        return parent
        
        
    def rootdeletion(self,root):    #when del target is root itself, the pointer is little different from other situations
        if root.right == None and root.left==None:      #so i build a rootdeletion function, make logic more clear
            root=None
                
        elif root.right != None and root.left == None:
            root=root.right
                
        elif root.left != None and root.right == None:
            root=root.left
        else:
            min=self.Min(root.right)
            if min==root.right:
                root.right.left=root.left
                root=root.right
                return root

            minparent=self.parent(root, min.val)
            # min is not the right child of Del
            if min.right==None:
                
                minparent.left=None
                   
            else:
                if minparent.left==min:
                    minparent.left=min.right
                else:
                    min.parent.right=min.right
            
            min.left=root.left
            min.right=root.right
            root=min
                
        return root

        
        
        
        
        #Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
        #Return the root node reference (possibly updated) of the BST.
        #Basically, the deletion can be divided into two stages:

        #1.Search for a node to remove.
        #2.If the node is found, delete the node.
        # Note: Time complexity should be O(height of tree).
