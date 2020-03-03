from collections import Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        cnter = Counter(nums)
        tail = {}
        
        for n in nums:
            # gap on this number
            if cnter[n] == 0:
                continue
            
            # if current number is expected as a tail, extend the tail
            elif tail.get(n, 0):
                tail[n] -= 1
                tail[n+1] = tail.get(n+1, 0) + 1
            
            # start a new array, add count to the expected tail position
            elif cnter.get(n+1, 0) and cnter.get(n+2, 0):
                cnter[n+1] -= 1
                cnter[n+2] -= 1
                tail[n+3] = tail.get(n+3, 0) + 1
            
            else:
                return False
            
            cnter[n] -= 1
        
        return True
    
'''
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

Solution: Greedy, Hashtable, traverse and mark
Time, Space: O(n)
'''
