class Solution(object):
    
    # two pointers
    def removeDuplicates(self, nums):        
        length = len(nums)
        if length < 2:
            return length
        
        p1, p2 = 0, 1
        
        while p2 != length:
            if nums[p1] == nums[p2]:
                p2+=1
            else:
                if p2-p1 == 1:
                    p2 += 1
                    p1 += 1
                else:
                    p1 += 1
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p2 += 1
        return p1 + 1
        
                
        
        """
        :type nums: List[int]
        :rtype: int
        """
        # Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
        # Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
