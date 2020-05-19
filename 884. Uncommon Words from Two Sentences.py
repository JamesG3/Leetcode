class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        dicA = {}
        dicB = {}
        
        for w in A.split(' '):
            dicA[w] = dicA.get(w, 0) + 1
        for w in B.split(' '):
            dicB[w] = dicB.get(w, 0) + 1
            
        res = set()
        for w, cnt in dicA.items():
            if w not in dicB and cnt == 1:
                res.add(w)
        for w, cnt in dicB.items():
            if w not in dicA and cnt == 1:
                res.add(w)
                
        return list(res)
    
'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Return a list of all uncommon words. 
You may return the list in any order.

Solution: Hashtable
Time: O(n)
Space: O(n)
'''
