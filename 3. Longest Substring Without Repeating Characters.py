from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        cur_len = 0
        cnt = {}
        queue = deque()
        
        for c in s:
            if cnt.get(c, 0) != 0:
                max_len = max(max_len, cur_len)
                while queue and queue[0] != c:
                    cc = queue.popleft()
                    cnt[cc] -= 1
                    cur_len -= 1
                queue.popleft()
                cnt[c] -= 1
                cur_len -= 1
                
            queue.append(c)
            cnt[c] = 1
            cur_len += 1
            
        return max(max_len, cur_len)
            
                
'''
Given a string, find the length of the longest substring without repeating characters.

Solution: Queue, deque, hashtable, edge case, sliding window
Time, Space: O(n)
'''
