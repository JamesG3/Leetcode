class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dic = {0: 1}
        counter = 0
        cur_sum = 0
        
        for n in nums:
            cur_sum += n
            if cur_sum - k in sum_dic:
                counter += sum_dic[cur_sum - k]
            if cur_sum not in sum_dic:            
                sum_dic[cur_sum] = 0
            sum_dic[cur_sum] += 1

        return counter
            
'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Solution: Hashtable, use diff between sums to calculate the interval's sum
Time, Space: O(n)
'''        

