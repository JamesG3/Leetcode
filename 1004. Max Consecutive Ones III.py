class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l, r = 0, 0
        length = len(A)
        mx_len = 0
        zero_cnt = 0
        
        while r < length:
            while r < length:
                if A[r] == 0:
                    if zero_cnt == K:
                        break
                    else:
                        zero_cnt += 1
                r += 1
                
            mx_len = max(mx_len, r - l)
            # move left cursor to the next element after the first 0 in current sliding window
            while l < r and A[l] == 1:
                l += 1
            l += 1
            zero_cnt -= 1
        return mx_len
'''
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s. 

Solution: Sliding windows, two pointers
Time: O(n)
Space: O(n)
'''
