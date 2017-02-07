class Solution(object):
    def findWords(self, words):
        line1 = list('qwertyuiopQWERTYUIOP')
        line2 = list('ASDFGHJKLasdfghjkl')
        line3 = list('zxcvbnmZXCVBNM')
        dic = {1:line1,2:line2,3:line3}
        
        ans = []
        
        for word in words:
            length = len(word)
            i = 0
            mark = 0                # mark where the last letter belongs to
            while i != length:
                if word[i] in line1:
                    if mark == 0:
                        mark = 1
                    elif mark != 1:
                        break
                elif word[i] in line2:
                    if mark == 0:
                        mark = 2
                    elif mark != 2:
                        break
                elif word[i] in line3:
                    if mark == 0:
                        mark = 3
                    elif mark != 3:
                        break
                i += 1
                
            if i == length:
                ans.append(word)
        return ans

                
                    
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        
        #Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
