class NumArray(object):

    def __init__(self, nums):
        self.dp = [0]
        self.nums = nums
        self.preCalculate()
        """
        :type nums: List[int]
        """
        
    def preCalculate(self):
        for i in xrange(len(self.nums)):
            self.dp.append(self.nums[i] + self.dp[-1])
        return
        
        

    def sumRange(self, i, j):
        return self.dp[j+1] - self.dp[i]
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)



# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
# You may assume that the array does not change.
# There are many calls to sumRange function.
