class Solution(object):
    def wordPattern(self, pattern, str):
        dic = {}
        index = 0
        length = len(pattern)
        str = str.split(" ")
        
        if length != len(str):      #if pattern's length is not same with the length of a sentence, it's false
            return False
        
        while index != length:
            if pattern[index] not in dic:
                for n in dic:           #check if a different pattern_mark's corresponding word is already saved in the dic
                    if dic[n] == str[index]:    #if pattern 'a' and 'b' point to a same word, it's false
                        return False
                dic[pattern[index]] = str[index]    #if no duplicate word, add the new pattern to the dic
            else:                                   #check if the corresponding word of the current pattern is right
                if str[index] != dic[pattern[index]]:
                    return False
            index += 1
            
        return True
        
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        
        #Given a pattern and a string str, find if str follows the same pattern.
        #Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
        #Examples:
        # pattern = "abba", str = "dog cat cat dog" should return true.
        # pattern = "abba", str = "dog cat cat fish" should return false.
        # pattern = "aaaa", str = "dog cat cat dog" should return false.
        # pattern = "abba", str = "dog dog dog dog" should return false.
