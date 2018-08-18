class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letters = [chr(n) for n in xrange(97, 123)]
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dic = dict(zip(letters, morse))
        
        pattern_set = set()
        for word in words:
            M = ''.join([dic[c] for c in word])
            if M not in pattern_set:
                pattern_set.add(M)
                
        return len(pattern_set)
