class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s, e = 0, len(nums)-1
        while s <= e:
            mid = (s + e) / 2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < nums[s]:
                if target <= nums[e] and target > nums[mid]:
                    s = mid+1
                else:
                    e = mid-1
                    
            else:
                if target < nums[mid] and target >= nums[s]:
                    e = mid - 1
                else:
                    s = mid + 1
        return -1
        
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
'''
