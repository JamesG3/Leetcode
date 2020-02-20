class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for word in words:
            dic[word] = dic.get(word, 0) + 1
        freq_list = sorted([[k, v] for k, v in dic.items()], key = lambda x: (-x[1], x[0]))
        return [w[0] for w in freq_list[:k]]

'''
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Solution: Hashtable, customized sort
Time: O(nlogn)
Space: O(n)
'''
