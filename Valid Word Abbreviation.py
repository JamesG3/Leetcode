class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        length_w = len(word)
        length_a = len(abbr)
        
        p = 0
        num = ''
        for i, c in enumerate(abbr):
            if c.isdigit():
                if num == '' and c == '0':          # to prevent corner cases like ["a"    "01"], which is not valid
                    return False
                num += c
            elif num != '':
                move = int(num)
                p += move
                num = ''
                if p < length_w:
                    if c != word[p]:
                        return False
                else:
                    return False
                p += 1
                
            else:                           # check the last part of string word
                if p < length_w:
                    if c != word[p]:
                        return False
                p += 1
        
        if num != '':
            move = int(num)
            p += move
        
        return p == length_w and i == length_a-1
                
                
        
        
        
        
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        
        
        # Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.
        # A string such as "word" contains only the following valid abbreviations:
        # ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
        # Give a string and a abbr, return whether it's a valid abbr
