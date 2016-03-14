# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if head is None:
            return head
        
        oddHead = head
        evenHead = head.next
        even = evenHead
        while evenHead and evenHead.next:
            oddHead.next = evenHead.next
            oddHead = oddHead.next
            evenHead.next = oddHead.next
            evenHead = evenHead.next
        oddHead.next = even
        return head
               
               
    # Still doubt
        #    else:
     #           b=head
     #           b.next=None
    #           return b
    #        head=head.next
           
            
 #       for n in head:
  #          if(n%2):
   #             a.append(n)
    #        else:
     #           b.append(n)
      #      head1=a+b
     
    
        """
        :type head: ListNode
        :rtype: ListNode
        """
