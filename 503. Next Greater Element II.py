class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n_nums = nums + nums
        length = len(nums)
        stack = []
        res = [-1 for _ in range(length)]
        
        for i, n in enumerate(n_nums):
            # invalid index after the orig nums
            if i >= length:
                index = None
            else:
                index = i
                
            if not stack or stack[-1][-1] >= n:
                stack.append([index, n])
                continue
            
            while stack and stack[-1][-1] < n:
                idx, m = stack.pop()
                # if index is not valid, change the corresponding res
                if idx != None:
                    res[idx] = n
            stack.append([index, n])
        return res

'''
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Solution: Stack, using double length of given nums to represent the circular array
Time: O(n)
Space: O(n)
'''
