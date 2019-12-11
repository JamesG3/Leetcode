class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        length = len(letters)
        s, e = 0, length - 1
        
        while s <= e:
            m = (s + e) // 2
            if letters[m] <= target:
                s = m + 1
            else:
                e = m - 1
                
        return letters[0] if s == length else letters[s]
'''
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Solution: Binary Search
Time: O(log(n))
Time: O(1)
'''
