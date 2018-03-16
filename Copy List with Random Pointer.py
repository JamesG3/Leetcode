# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return
        
        newhead = RandomListNode(head.label)
        node = newhead
        
        while head.next:
            nextnode = RandomListNode(head.next.label)
            node.next = nextnode
            if head.random:
                nextrandomnode = RandomListNode(head.random.label)
                node.random = nextrandomnode
            head = head.next
            node = node.next
            
        if head.random:                     # last node
            nextrandomnode = RandomListNode(head.random.label)
            node.random = nextrandomnode
            
        return newhead
        
                
                
        
        
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        
      # A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
      # Return a deep copy of the list.
