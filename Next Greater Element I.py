class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        ans = []
        length = len(nums)
        
        for n in findNums:
            i = nums.index(n)           #get every index of n in the nums
            while i != length:          #for every item after n
                if nums[i]>n:
                    ans.append(nums[i])
                    break
                i+=1
            if i == length:             #if not find, append -1
                ans.append(-1)
        return ans
            
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
        #The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

