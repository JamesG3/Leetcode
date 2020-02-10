class Node:
    def __init__(self, valid):
        self.valid = valid
        self.child = {}

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(False)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.head
        for c in word:
            if c not in node.child:
                node.child[c] = Node(False)
            node = node.child[c]
        node.valid = True
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.head
        dfs = [node]
        for c in word:
            tmp_dfs = []
            if c == '.':
                for node in dfs:
                    for k,v in node.child.items():
                        tmp_dfs.append(v)
            else:
                for node in dfs:
                    if c in node.child:
                        tmp_dfs.append(node.child[c])
            dfs = tmp_dfs
            
        return any([node.valid for node in dfs])
                
            
                
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


'''
Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Solution: Trie, BFS
'''
