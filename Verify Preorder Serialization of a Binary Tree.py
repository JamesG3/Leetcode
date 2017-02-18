class Solution(object):
    def isValidSerialization(self, preorder):
        nullcounter = 0                 #counter for null nodes
        numbercounter = 0               #counter for nodes which are not null
        preorder = preorder.split(',')
        
        length = len(preorder)
        if length == 1 and preorder[0]=="#":            #an enpty tree
            return True
        elif length == 2 or length == 0:                #the length cannot be 2 or 0
            return False
        else:                       #if there are more than three elements in the tree,then the last two elements must be '#'
            if preorder[-1] != "#" or preorder[-2] != "#":
                return False
                
        preorder = preorder[:-2]    #delete the last two elements
        
        for item in preorder:
            if item.isalnum():      #if the current node is not null, then numbercounter add 1
                numbercounter += 1
            elif item == "#":       #if the current node is null, the nullcounter add 1
                nullcounter += 1
            
            if numbercounter < nullcounter: #compare the two counters in every loop, make sure the numbercounter >= nullcounter
                return False
                
        if numbercounter-nullcounter == 1:  #when the loop ends, for a binary tree, the number of null nodes is 1 more than the number of not null nodes. Because we already delete two null nodes, so (numbercounter-nullcounter) should equals 1
            return True
        else:
            return False
        
        """
        :type preorder: str
        :rtype: bool
        """
        
        
        #One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.
