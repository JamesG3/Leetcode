# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        pre = slow = fast = head
        
        # use two pointers to find the left part and right part of the linked list
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        # detach the part1 and part2
        pre.next = None
        
        # recursive detach nodes
        n1 = self.sortList(head)
        n2 = self.sortList(slow)
        
        # start merge sort from two single nodes
        return self.merge_sort(n1, n2)
        
    # merge two independent linked list
    def merge_sort(self, n1, n2):
        tmp_head = ListNode(0)
        nd = tmp_head
        
        while n1 and n2:
            if n1.val < n2.val:
                nd.next = n1
                n1 = n1.next
            else:
                nd.next = n2
                n2 = n2.next
            nd = nd.next
        if n1:
            nd.next = n1
        else:
            nd.next = n2
        return tmp_head.next
        
        
'''
Sort a linked list in O(n log n) time using constant space complexity.

Solution: Two pointers, merge sort, linked list operation
Time: O(nlogn)
Space: O(1)
'''
