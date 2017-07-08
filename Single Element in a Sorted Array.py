class Solution(object):
    def singleNonDuplicate(self, nums):
        high = len(nums)-1
        low = 0
                                        # binary search
        while low<high:
            mid = low + (high-low)/2
            if mid<nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            elif mid%2 == 0 and nums[mid] == nums[mid+1]:
                low = mid+1
            elif mid%2 == 1 and nums[mid] == nums[mid-1]:
                low = mid+1
            else:
                high = mid-1
        return nums[low]
                
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.
        # Note: Your solution should run in O(log n) time and O(1) space.
