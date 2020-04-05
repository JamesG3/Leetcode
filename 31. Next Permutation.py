class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        
        not_found = True
        
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                not_found = False
                break
        
        if not_found:
            nums[:] = nums[::-1]
            return
        
        min_large, min_large_i = float('inf'), None
        swap_a = nums[i-1]
        for j, b in enumerate(nums[i:]):
            if b > swap_a and b < min_large:
                min_large, min_large_i = b, j+i
        
        nums[i-1], nums[min_large_i] = min_large, swap_a
        nums[:] = nums[:i] + sorted(nums[i:])
        return
    
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

Solution: Traverse and mark, math, array, in-place
Time: O(n)
Space: O(1)
'''
            
        
