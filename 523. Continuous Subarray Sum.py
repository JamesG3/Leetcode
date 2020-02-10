class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        range_sum = {0: -1}
        cur_sum = 0
        for i, n in enumerate(nums):
            cur_sum += n
            if k != 0:
                cur_sum = cur_sum % k

            # if the result of (cur_sum % k) is in dict
            # which means there is a previous n can be substracted from current range_sum
            if cur_sum in range_sum:
                # size at least 2 that sums up to a multiple of k
                if i - range_sum[cur_sum] > 1:
                    return True
            else:
                range_sum[cur_sum] = i
            
        return False
            
            
'''
Given a list of non-negative numbers and a target integer k, 
write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, 
that is, sums up to n*k where n is also an integer.

Solution: Math, Hashtable, edge case
Time, Space: O(n)
'''    
        
