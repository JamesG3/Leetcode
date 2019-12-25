class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index_dic = {0:-1}
        max_len = 0
        cur_sum = 0
        
        for i, n in enumerate(nums):
            if n == 0:
                cur_sum -= 1
            else:
                cur_sum += 1
                
            if cur_sum not in index_dic:
                index_dic[cur_sum] = i
            else:
                max_len = max(max_len, i - index_dic[cur_sum])
                
        return max_len
        
        
'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Solution: Hashtable, 0 -> -=1; 1 -> +=1, save every cur_sum in hashtable, calculate & update the index distance
Time, Space: O(n)
'''
