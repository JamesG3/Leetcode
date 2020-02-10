class PrefixNode:
    def __init__(self, c: str, valid: bool):
        self.next = {}
        self.valid = valid
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = PrefixNode('', False)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.head
        for c in word:
            if c not in node.next:
                node.next[c] = PrefixNode(c, False)
            node = node.next[c]
        node.valid = True
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.head
        for c in word:
            if c not in node.next:
                return False
            node = node.next[c]
        return node.valid
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.head
        for c in prefix:
            if c not in node.next:
                return False
            node = node.next[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
