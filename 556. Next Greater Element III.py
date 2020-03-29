class Solution:
    def nextGreaterElement(self, n: int) -> int:
        numstr = list(str(n))
        tmp_nums = []
        
        for i in range(len(numstr)):
            if i == len(numstr) - 1:
                break
            tmp_nums.append(numstr[~i])
            if numstr[~i] > numstr[~(i+1)]:
                break
        
        if i == len(numstr) - 1:
            return -1

        target = numstr[~(i+1)]
        minlarge = '9'
        minlarge_i = None
        for i, n in enumerate(tmp_nums):
            if n > target and n <= minlarge:
                minlarge = n
                minlarge_i = i
        
        
        tmp_nums[minlarge_i] = target
        numstr[~(i+1)] = minlarge
        numstr[~i:] = sorted(tmp_nums)
        final_num = int(''.join(numstr))
        return final_num if final_num < 2**31 else -1
     
'''
Solution: 
    1. traverse from the end
    2. find the first decreasing element
    3. swap this element with the smallest number in the rest of string (need to be larger than this element)
    4. sort the rest of elements in asc order
    5. replace the orig substring with this ordered str
    6. check if the result if invalid (if >= than 2 ** 31)
    
Time: O(1)
Space: O(1)
'''
