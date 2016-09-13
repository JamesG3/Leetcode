class Solution(object):
    def searchRange(self, nums, target):
        r=[]
        n=0
        if target not in nums:
            r=[-1,-1]
            return r
        else:
            while nums[n]!=target:
                n+=1
            r.append(n)
            while nums[n]==target:
                if n+1<len(nums):
                    if nums[n+1]==nums[n]:
                        n+=1
                    else:
                        break
                else:
                    break
            r.append(n)
        return r
                
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Given a sorted array of integers, find the starting and ending position of a given target value.

        Your algorithm's runtime complexity must be in the order of O(log n).

        If the target is not found in the array, return [-1, -1].

        For example,
        Given [5, 7, 7, 8, 8, 10] and target value 8,
        return [3, 4].
        """
