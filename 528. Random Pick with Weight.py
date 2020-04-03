import random
class Solution:

    def __init__(self, w: List[int]):
        self.freq = []
        cur = 0
        for f in w:
            cur += f
            self.freq.append(cur)
        

    def pickIndex(self) -> int:
        num = random.randint(0, self.freq[-1])
        l, r = 0, len(self.freq)-1
        while l != r:
            m = (l + r) // 2
            if self.freq[m] <= num:
                l = m+1
            else:
                r = m
        return l
                
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

'''
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.

Solution: Binary Search
Time: O(log(n)) - n is the length of w
Space: O(n) - n is the size of w

'''
