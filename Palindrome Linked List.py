# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        fast = head
        slow = head
        
        if head is None:
            return True
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        count = 0               #a counter used for count the length of each part
        original_head = head    #start of right part of Palindrome  
                                #head will be the start of left part
        while slow.next != None:    #move numbers to head using reverse order
            tem = slow.next         #make left part and right part in same order
            slow.next = slow.next.next
            tem.next = head
            head = tem
            count+=1
            
        for n in xrange(count):     #compare every number to check if the corresponding numbers are same
            if head.val != original_head.val:   #if not, then it's not a Palindrome
                return False
            else:
                head = head.next
                original_head = original_head.next
                
        if original_head.next == None:  #if there is only one number in the middle, then it's a Palindrome
            return True
        else:                           #if there are two numbers in the middle
            if original_head.val == original_head.next.val:     #if this two numbers are same, then it's a Palindrome
                return True
            else:                       #if different, False 
                return False
            
        """
        :type head: ListNode
        :rtype: bool
        """
        #Given a singly linked list, determine if it is a palindrome.
        #Could you do it in O(n) time and O(1) space?
