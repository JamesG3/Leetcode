# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodea, nodeb = headA, headB
        lena, lenb = 0, 0
        
        # first traverse, find lengths and compare the last node
        while nodea and nodea.next:
            nodea = nodea.next
            lena += 1
        while nodeb and nodeb.next:
            nodeb = nodeb.next
            lenb += 1
            
        # if the last node is not same, for sure there is no intersection
        if nodea != nodeb:
            return None
        
        # second traverse, make the two linkedlist same length, then traverse one node by on node
        nodea, nodeb = headA, headB
        if lena > lenb:
            lng, srt = nodea, nodeb
        else:
            lng, srt = nodeb, nodea
                
        for i in range(abs(lena - lenb)):
            lng = lng.next
            
        while lng != srt:
            lng = lng.next
            srt = srt.next
        
        return srt
        
'''
Write a program to find the node at which the intersection of two singly linked lists begins.
Solution: Two traverses, linked list operation, two pointers
Time: O(n)
Space: O(1)
'''
