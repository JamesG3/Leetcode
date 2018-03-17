class Node(object):
    def __init__(self):
        self.children = {}
        self.word = False
        
class Trie:

    def __init__(self):
        self.root = Node()
        
        """
        Initialize your data structure here.
        """
        
    def insert(self, word):
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                child = Node()
                node.children[w] = child
                node = node.children[w]
        node.word = True
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        
    def search(self, word):
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                return False
        return node.word
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
    def startsWith(self, prefix):
        node = self.root
        for w in prefix:
            if w in node.children:
                node = node.children[w]
            else:
                return False
        return True
        
        
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
