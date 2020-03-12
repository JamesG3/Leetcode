import random
import copy

class Solution:

    def __init__(self, nums: List[int]):
        self.orig_nums = nums
        self.length = len(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.orig_nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = []
        tmp_nums = copy.deepcopy(self.orig_nums)
        for i in range(self.length):
            swap_i = random.randint(i, self.length-1)
            tmp_nums[swap_i], tmp_nums[i] = tmp_nums[i], tmp_nums[swap_i]
        
        return tmp_nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
