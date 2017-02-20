# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        listA = []
        listB = []
        
        if headA==None or headB==None:
            return None
        
        temA = headA
        temB = headB
        
        while temA != None:             #save all value into the corresponding list
            listA.append(temA.val)
            temA = temA.next
        while temB != None:
            listB.append(temB.val)
            temB = temB.next
            
        lengthA = len(listA)
        lengthB = len(listB)
        
        listA = listA[::-1]             #reverse two lists
        listB = listB[::-1]
        
        i = 0
        while i<lengthA and i<lengthB:  #find the intersection part
            if listA[i] != listB[i]:
                break
            i+=1
            
        countdown = lengthA - i         #calculate how many step to move to find the first intersection node
        while countdown != 0:
            headA = headA.next
            countdown -= 1
        return headA
            
            
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        
        #Write a program to find the node at which the intersection of two singly linked lists begins.
