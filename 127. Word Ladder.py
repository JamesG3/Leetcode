class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = {}
        # build graph O(n)
        length = len(beginWord)
        for word in wordList:
            for i in range(length):
                k = '{}?{}'.format(word[:i], word[i+1:])
                if k not in graph:
                    graph[k] = set()
                graph[k].add(word)
                
        times = 0
        visted = set()
        bfs = set([beginWord])
        # bfs to get the minimal depth: O(n)
        while bfs:
            tmp_bfs = set()
            times += 1
            for word in bfs:
                if word in visted:
                    continue
                    
                visted.add(word)
                if word == endWord:
                    return times
                
                for i in range(length):
                    k = '{}?{}'.format(word[:i], word[i+1:])
                    tmp_bfs = tmp_bfs.union(set(graph.get(k, set())))
                
                graph[word] = set()
            bfs = tmp_bfs
        
        return 0
    
'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Solution: Hashtable, BFS
Time, Space: O(word_length * n)
'''

