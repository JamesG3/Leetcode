# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = l1
        t = l1
        while l1 != None and l2 != None:
            l1.val = l1.val + l2.val
            if l1.val >= 10:
                l1.val = l1.val % 10
                if l1.next != None:         #if next digit should add 1, judge which situation.
                    l1.next.val +=1
                else:                       #one more listnode should be added
                    tem=ListNode(1)
                    l1.next = tem
            
            if l1.next is None and l2.next is not None:     #if l2 is longer, add l2.next to l1.next, link them together.
                l1.next = l2.next
                break
            
            elif l1.next is not None and l2.next is None:   #if l1 is longer, judge whether next digit should be added 1.
                while l1 is not None:                   #check all rest part of l1, to find if there is a digit need to add.
                    
                    if l1.val >= 10:
                        l1.val = l1.val % 10
                        if l1.next != None:
                            l1.next.val +=1
                            
                        else:
                            tem=ListNode(1)
                            l1.next = tem
                    l1=l1.next
                    
            else:                       #corresponding with the first if
                l1 = l1.next
                l2 = l2.next
        
        return head
            
        """
        :type l1: ListNodet
        :type l2: ListNode
        :rtype: ListNode
        
        You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        """
        
