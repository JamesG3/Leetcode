class Solution(object):

    def __init__(self, nums):
        self.nums=nums
        
        """
        :type nums: List[int]
        :type size: int
        """
        

    def reset(self):
        return self.nums
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        

    def shuffle(self):
        return random.sample(self.nums,len(self.nums))      #using random sampling to shuffle
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
