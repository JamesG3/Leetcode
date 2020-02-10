class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        dist = {}
        for i, n in enumerate(words):
            if n not in dist:
                dist[n] = []
            dist[n].append(i)
            
        i1, i2 = dist[word1], dist[word2]
        min_dist = float('inf')
        
        if word1 == word2:
            i = dist[word1]
            if len(i) > 1:
                p1, p2 = 0, 1
                while p2 < len(i):
                    min_dist = min(min_dist, i[p2] - i[p1])
                    p1 += 1
                    p2 += 1
            
        else:
            p1, p2 = 0, 0
            while p1 < len(i1) and p2 < len(i2):
                min_dist = min(min_dist, abs(i1[p1] - i2[p2]))
                if i1[p1] < i2[p2]:
                    p1 += 1
                else:
                    p2 += 1        
        return min_dist
            
'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
word1 and word2 may be the same and they represent two individual words in the list.

Solution: Hashtable, two pointers, conditions, greedy
Time, Space: O(n)
'''
