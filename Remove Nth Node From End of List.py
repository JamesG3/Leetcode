# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        count=0
        tem1=head
        tem2=head
        while tem1 != None:
            count+=1
            tem1=tem1.next
        if count==n:
            return head.next
            
        for n in range(0,count-n-1):
            tem2=tem2.next
        tem2.next=tem2.next.next
        
        return head
        
        
        """
        temH = head
        temE = head

        for i in range(0,n):
            temE = temE.next
            if(temE == None):
                return head.next
        while(temE.next != None):
            temE = temE.next
            temH = temH.next
            print temE.val
            print temH.val
        temH.next = temH.next.next
        return head
        """
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        
        Given a linked list, remove the nth node from the end of list and return its head.
        """
        
