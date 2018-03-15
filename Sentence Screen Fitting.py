class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        currIndex = 0
        sentence = "-".join(sentence) + "-"
        length = len(sentence)
        
        for i in xrange(rows):
            currIndex += cols
            while sentence[currIndex % length] != "-":
                currIndex -= 1      # if single line cannot store the whole word, then backspace, ignore those wasted space
            currIndex += 1
        return currIndex / length
        
        
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        
