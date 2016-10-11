# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        if head == None:
            return head
            
        First = ListNode(0)                     #build a very first head before current head
        First.next = head
        tem = head
        
        while tem.next != None:                 #go through the list
            if tem.next.val < tem.val:          #if the sequence is not right
                F = First
                while F.next.val < tem.next.val:    #compare each number from the head, to find the position to insert
                    F = F.next
                tn = tem.next                      #insert.  (pay attation to the insert sequence)
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
        
