class Solution(object):
    def maxProduct(self, words):
        dic = {}
        
        for word in words:
            tem = 0
            for c in word:
                tem |= 1 << (ord(c)-ord('a'))   # different digit represent different letters
            dic[word] = tem
        
        M = 0
        for i in dic:
            for j in dic:
                if dic[i] & dic[j] == 0:    # if the result of & operation is 0, means there is no duplicate letters between this two words
                    M = max(len(i)*len(j), M)
        return M
        
        
        """
        :type words: List[str]
        :rtype: int
        """
        
        
        
        #Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
        #Using bit map
