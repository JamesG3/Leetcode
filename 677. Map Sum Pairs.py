class Node:
    def __init__(self):
        self.val = 0
        self.child = {}
    
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for c in key:
            if c not in node.child:
                node.child[c] = Node()
            node = node.child[c]
        node.val = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.child:
                return 0
            else:
                node = node.child[c]
        bfs = [node]
        res = node.val
        
        while bfs:
            tmp_bfs = []
            for node in bfs:
                tmp_bfs += list(node.child.values())
                res += sum([n.val for n in list(node.child.values())])
            bfs = tmp_bfs
        return res
            
        
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


'''
Implement a MapSum class with insert, and sum methods.
For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.
For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Solution: Trie, Prefix tree, BFS
'''
