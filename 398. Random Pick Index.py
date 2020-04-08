class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = -1
        for i, v in enumerate(self.nums):
            if v == target:
                count+=1
                rand = random.randint(1,count)
                if rand == 1:
                    res = i
        return res
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

'''


Solution: Reservoir Sampling, math, random, prob
    traverse the nums, add 1 to counter everytime we see a number == target
    the prob of each randint==1 will be: 1, 1/2, 1/3, 1/4 ....
    we always use the latter one as the result index if randint==1
    in this case, the prob of each index would be: 1/n, ..., 1/(n-1) * (n-1)/n, 1/n
    the prob are all equal
    
Time: O(n)
Space: O(1)
'''

