class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = []
        for word in d:
            p1, p2 = 0, 0
            while p1 < len(s) and p2 < len(word):
                if s[p1] == word[p2]:
                    p2 += 1
                p1 += 1
            if p2 == len(word):
                res.append(word)
        return sorted(res, key = lambda x: (-len(x), x))[0] if res else ''
                
'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Solution: Traverse, sort
Time: O(m*n)
Space: O(n)
'''
