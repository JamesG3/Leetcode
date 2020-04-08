class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {c:v for v,c in enumerate(order)}
        return words == sorted(words, key=lambda x: [dic[_] for _ in x])
            
'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.


Solution: Customized ordering
Time: O(nlogn)
Space: O(n)
'''
