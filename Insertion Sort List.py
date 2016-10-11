# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        if head == None:
            return head
            
        First = ListNode(0)
        First.next = head
        tem = head
        
        while tem.next != None:
            if tem.next.val < tem.val:
                F = First
                while F.next.val < tem.next.val:
                    F = F.next
                tn = tem.next
                tem.next = tem.next.next
                tn.next = F.next
                F.next = tn
            else:
                tem = tem.next
                
        return First.next
                
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
