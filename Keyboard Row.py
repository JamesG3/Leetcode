class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dic = {}
        res = []
        for c in 'QWERTYUIOP':
            dic[c] = 1
        for c in 'ASDFGHJKL':
            dic[c] = 2
        for c in 'ZXCVBNM':
            dic[c] = 3
            
        for word in words:
            tmp = 0
            flag = 0
            for c in word:
                if not tmp:
                    tmp = dic[c.upper()]
                else:
                    if tmp != dic[c.upper()]:
                        flag = 1
                        break
            if flag == 0:
                res.append(word)
                
        return res
                
                    
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        
        #Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
