# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1!=None or l2!=None:
            if l2==None or (l1!=None and l2.val>=l1.val):
                tem=l1
                tem.next=self.mergeTwoLists(l1.next,l2)
            else:
                tem=l2
                tem.next=self.mergeTwoLists(l1,l2.next)
                
            return tem
        else:
            return None
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: 
        Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
        """
