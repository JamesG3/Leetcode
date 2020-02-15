class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_dict = {}
        res_max = 1
        for word in sorted(words, key=lambda x: len(x)):
            length = len(word)
            if length not in word_dict:
                word_dict[length] = []
                
            if length-1 in word_dict:
                tmp_max = 1
                for p_w, p_cnt in word_dict[length-1]:
                    if self.if_pre(p_w, word):
                        tmp_max = max(tmp_max, p_cnt + 1)
                word_dict[length].append([word, tmp_max])
                res_max = max(res_max, tmp_max)
            
            else:
                word_dict[length].append([word, 1])
        return res_max
        
        
    def if_pre(self, word_prev, word_next):
        counter = 0
        p1, p2 = 0, 0
        while p1 < len(word_prev) and p2 < len(word_next):
            if word_prev[p1] != word_next[p2]:
                p2 += 1
                counter += 1
            else:
                p1 += 1
                p2 += 1
        # differece in the middle / the last one is different
        return counter == 1 or p2 == p1
    
'''
Given a list of words, each word consists of English lowercase letters.
Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".
A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
Return the longest possible length of a word chain with words chosen from the given list of words.

Solution: Hashtable, DP, Greedy, Two pointers, edge case
Time: max-O(n**2), min-O(n)
Space: O(n)
'''
