class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedlst = sorted(nums)
        l, r = -1, len(nums)
        for i in range(len(nums)):
            if nums[i] == sortedlst[i]:
                l = i
            else:
                break
                
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == sortedlst[i]:
                r = i
            else:
                break
    
        return max(r - 1 - l, 0)
            
'''
Solution: Sort, two pointers
Time: O(nlogn)
Space: O(n)
'''    

            
        
