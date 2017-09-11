class MagicDictionary(object):

    def __init__(self):
        self.dic = {}
        """
        Initialize your data structure here.
        """
        

    def buildDict(self, dict):
        for word in dict:
            L = len(word)
            if L not in self.dic:
                self.dic[L] = [word]
            else:
                self.dic[L].append(word)
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        

    def search(self, word):
        if len(word) in self.dic:
            return self.compare(word, self.dic[len(word)])
        else:
            return False
        
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        
    def compare(self, word, wordlist):
        for W in wordlist:
            if word != W:
                counter = 0
                index = 0
                while counter < 2 and index < len(word):
                    if word[index] != W[index]:
                        counter += 1
                    index += 1
                if counter == 1:
                    return True
        return False
                    
            


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)


# Implement a magic directory with buildDict, and search methods.
# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
# For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.
