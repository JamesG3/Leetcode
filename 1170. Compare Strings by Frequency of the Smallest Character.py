class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        word_cnt = [self.get_cnt(w) for w in words]
        res = []
        for q in queries:
            q_cnt = self.get_cnt(q)
            res.append(len(list(filter(lambda x: x>q_cnt, word_cnt))))
        return res
        
    def get_cnt(self, string):
        target = sorted(list(set(string)))[0]
        return string.count(target)
    
    
'''
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.
Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

Solution: Hasttable, (binary search) if need improve performance
Time: O(n * m)
Space: O(m)
'''

