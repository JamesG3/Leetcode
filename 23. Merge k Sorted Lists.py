import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        fkhead = ListNode(-1)
        head = fkhead
        n_dic = {}
        heap = []
        
        # create a heap to store all heads' vals
        for n in lists:
            if not n:
                continue
            heap.append(n.val)
            n_dic[n.val] = n_dic.get(n.val, []) + [n]
        heapq.heapify(heap)
        
        while heap:
            sml_val = heapq.heappop(heap)
            # pop all the nodes with same val from the heap
            while heap:
                nxt_val = heapq.heappop(heap)
                if nxt_val != sml_val:
                    heapq.heappush(heap, nxt_val)
                    break
            
            # get all nodes with same val 
            sml_nodes = n_dic[sml_val]
            del n_dic[sml_val]
            
            # add these nodes into the linkedList, push their next nodes into heap
            for sml_node in sml_nodes:
                nxt_node = sml_node.next
                sml_node.next = None
                
                if nxt_node:
                    heapq.heappush(heap, nxt_node.val)
                    n_dic[nxt_node.val] = n_dic.get(nxt_node.val, []) + [nxt_node]
                    
                head.next = sml_node
                
                head = head.next
        
        return fkhead.next
        
        
'''
Solution: Heap, LinkedList, priority queue
Time: O(mlog(n)), m is the total number of nodes, n is the nubmer of heads
Space: O(n), need a heap to store all current status

'''
