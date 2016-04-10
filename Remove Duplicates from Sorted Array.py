class Solution(object):
    def removeDuplicates(self, nums):
        #count=0
        #while(count<len(nums)-1):
        #    if(nums[count]==nums[count+1]):
        #        nums.remove(nums[count])
        #    else:
        #        count+=1
        #return len(nums)
        if nums == []: return 0
        left = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[left]:
                if left + 1 < i:
                    nums[left+1] = nums[i]
                left += 1
        del nums[left+1:]
        return len(nums) 
                
        """
        :type nums: List[int]
        :rtype: int
        """
        #Given a sorted linked list, delete all duplicates such that each element appear only once. 
