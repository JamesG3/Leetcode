class WordDistance:

    def __init__(self, words: List[str]):
        self.dist = {}
        self._get_index(words)
        
        
    def _get_index(self, words):
        for i, w in enumerate(words):
            if w not in self.dist:
                self.dist[w] = []
            self.dist[w].append(i)


    def shortest(self, word1: str, word2: str) -> int:
        in_1, in_2 = self.dist[word1], self.dist[word2]
        p1, p2 = 0, 0
        min_dist = float('inf')
        
        while p1 < len(in_1) and p2 < len(in_2):
            i1, i2 = in_1[p1], in_2[p2]
            min_dist = min(min_dist, abs(i1 - i2))
            
            if i1 > i2:
                p2 += 1
            else:
                p1 += 1
                
        return min_dist
            
        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

'''
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Solution: Hashtable, two pointers, single traverse
Time:O(n) to initialize, O(n) to calculate dist
Space: O(n)
'''
