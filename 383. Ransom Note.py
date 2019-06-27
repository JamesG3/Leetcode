from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ran_cnt = Counter(ransomNote)
        mag_cnt = Counter(magazine)
        
        for k,v in ran_cnt.items():
            if k not in mag_cnt:
                return False
            
            if v > mag_cnt[k]:
                return False
            
        return True
        
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; 
# otherwise, it will return false.
# Each letter in the magazine string can only be used once in your ransom note.
