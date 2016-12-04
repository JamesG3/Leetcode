# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if head is None:            #if the head is None, prevent the underflow
            return head
        
        k=k%self.count(head)        #calculate the module of k % length, prevent the overflow
        x=head
        y=head
        
        while k!=0:                 #x starts k steps before y
            x=x.next
            k-=1
        while x.next != None:       #x and y moving to next node together
            x=x.next
            y=y.next
            
        x.next=head                 #swap head, tail and rotate point
        head=y.next
        y.next=None
        return head
        
        
    def count(self, head):      #k might be larger than the number of nodes
        counter=0
        tem=head
        while tem!=None:
            counter+=1
            tem=tem.next
        return counter
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        #Given a list, rotate the list to the right by k places, where k is non-negative.
        #For example:
        #Given 1->2->3->4->5->NULL and k = 2,
        #return 4->5->1->2->3->NULL.
        #Notice: k might be larger than the number of nodes.
        
