class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        dic = {}
        
        def getRoot(w):
            while w != dic[w]: 
                w = dic[w]
            return w
        
        for w1, w2 in pairs:
            if w1 in dic and w2 in dic:
                dic[getRoot(w2)] = getRoot(w1)
            elif w1 in dic:
                dic[w2] = getRoot(w1)
            elif w2 in dic:
                dic[w1] = getRoot(w2)
            else:
                dic[w1] = w2
                dic[w2] = w2
                
                
        length1 = len(words1)
        length2 = len(words2)
        
        if length1 != length2:
            return False

        for i in xrange(length1):
            if words1[i] == words2[i]:
                continue
            if words1[i] not in dic or words2[i] not in dic:
                return False
            if getRoot(words1[i]) != getRoot(words2[i]):
                return False
        
        return True
        
        
            
        
            
        
        
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        
        
        # similiar with Sentence Similarity, except the similarity relation is transitive.
