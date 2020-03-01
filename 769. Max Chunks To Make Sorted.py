class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cur_max = 0
        cnt = 0
        
        for i, n in enumerate(arr):
            # we can chunk the arr only if the index equals the max number in the current subarray
            cur_max = max(cur_max, n)
            if i == cur_max:
                cnt += 1
        return cnt
            
'''
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.
What is the most number of chunks we could have made?

Solution: Traverse, list, Math
Time: O(n)
'''
