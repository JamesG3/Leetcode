# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
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
                print t.val
                
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
        
