# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # iterative solution
    def reverseList(self, head):

        if not head:
            return head
        
        tmp1 = None
        
        while head:
            tmp2 = head
            head = head.next
            tmp2.next = tmp1            
            tmp1 = tmp2
        return tmp2
        
    # recursive solution
#     def reverseList(self, head):
    
#         return self.helper(head, None)
    
#     def helper(self, node, prev):
#         if not node:
#             return prev
        
#         tmp = node.next
#         node.next = prev
        
#         return self.helper(tmp, node)
              
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
