# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp_head = head
        prev = None
        node = head
        
        while node and node.next:
            nxt = node.next
            node.next = node.next.next
            nxt.next = node
            if not prev:
                tmp_head = nxt
            else:
                prev.next = nxt
            prev = node
            node = node.next
            
        return tmp_head
            

'''
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.
Time: O(n)
Space: extra O(1)
'''
