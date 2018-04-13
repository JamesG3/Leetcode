class Solution(object):
    
    # two pointers solution
    def removeElement(self, nums, val):
        length = len(nums)
        if length == 0:
            return length
        elif length == 1:
            return 0 if nums[0] == val else 1
            
        p1, p2 = 0, 1
        
        while p2 < length:
            if nums[p1] != val:
                p1 += 1
                p2 += 1
            else:
                if nums[p2] != val:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 += 1
                    p2 += 1
                else:
                    p2 += 1
        
        return p1+1 if nums[p1] != val else p1
        
        
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        # Given an array nums and a value val, remove all instances of that value in-place and return the new length.
        # Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        # The order of elements can be changed. It doesn't matter what you leave beyond the new length.
