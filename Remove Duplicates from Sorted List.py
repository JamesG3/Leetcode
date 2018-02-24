# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # two pointers solution
    def deleteDuplicates(self, head):
        fast, slow = head, head
        
        if not head or not head.next:
            return head
        
        fast = fast.next
        
        while fast:
            if slow.val == fast.val:
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next
            
        return head
    
    
    # recursive solution
    def deleteDuplicates(self, head):
        tem=head
        if tem == None:
            return head
        
        else:
            self.compare(tem)
        return head

        
    def compare(self, t):
        if t != None and t.next != None:
            if t.val == t.next.val:
                t.next = t.next.next
                
                if t != None and t.next != None:
                    if t.val == t.next.val:
                        self.compare(t)
                    else:
                        self.compare(t.next)
            else:
                    self.compare(t.next)
        else:
            return t
            
            
        """
        :type head: ListNode
        :rtype: ListNode
        Given a sorted linked list, delete all duplicates such that each element appear only once.
        """
        
