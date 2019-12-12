class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        
        for n in nums2:
            if not stack or n < stack[-1]:
                stack.append(n)
                continue
                
            while stack and n > stack[-1]:
                dic[stack.pop()] = n
            stack.append(n)
        
        # pop the rest of elements
        while stack:
            dic[stack.pop()] = -1
            
        return [dic[n] for n in nums1]
    
'''
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Solution: Stack
Time & Space: O(n + m)
'''
