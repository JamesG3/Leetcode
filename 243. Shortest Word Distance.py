class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        dist = {}
        for i, n in enumerate(words):
            if n not in dist:
                dist[n] = []
            dist[n].append(i)
            
        i1, i2 = dist[word1], dist[word2]
        p1, p2 = 0, 0
        min_dist = float('inf')
        
        while p1 < len(i1) and p2 < len(i2):
            min_dist = min(min_dist, abs(i1[p1] - i2[p2]))
            if i1[p1] > i2[p2]:
                p2 += 1
            else:
                p1 += 1
        
        return min_dist

'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Solution: Hashtable, two pointers
Time, Space: O(n)
'''
