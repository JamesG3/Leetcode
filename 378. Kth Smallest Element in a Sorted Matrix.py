import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return None
        
        N = len(matrix)
        heap = [(m[0], i, 0) for i, m in enumerate(matrix)]
        heapq.heapify(heap)
        
        for i in range(k-1):
            n, m_i, r_i = heapq.heappop(heap)
            if r_i == N-1:
                continue
            
            heapq.heappush(heap, (matrix[m_i][r_i+1], m_i, r_i+1))
            
        res, _, _ = heapq.heappop(heap)
        return res
    
'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Solution: Heap, maintain a min heap with size n (contains at most one element in each row), update it k-1 times, the heap top is the res
Time: O(nlogn)
Space: O(n)
'''
