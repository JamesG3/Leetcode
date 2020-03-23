class Node:
    def __init__(self):
        self.is_sent = False
        self.next = {}
        self.sent = None
        self.hot = 0
    
class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Node()
        self.initTree(sentences, times)
        self.cur_sent = ''
            
    # the first traversal on the given sentences and times
    def initTree(self, sentences, times):
        for i, sentence in enumerate(sentences):
            self.insert(sentence, times[i])
    
    # insert a sentence with it's time
    def insert(self, sentence, time):
        node = self.root
        for c in sentence:
            if c not in node.next:
                new_node = Node()
                node.next[c] = new_node
            node = node.next[c]
        node.is_sent = True
        node.sent = sentence
        node.hot += time
    
    # search base on the current self.cur_sent
    def search(self):
        res = []
        node = self.root
        for c in self.cur_sent:
            # no result found
            if c not in node.next:
                return []
            node = node.next[c]
        bfs = [node]
        while bfs:
            tmp_bfs = []
            for n in bfs:
                if n.is_sent:
                    res.append([n.sent, n.hot])
                for k, v in n.next.items():
                    tmp_bfs.append(v)
            bfs = tmp_bfs
        
        if not res:
            return []
        
        top3 = sorted(res, key = lambda x: (-x[1], x[0]))[:3]
        return [_[0] for _ in top3]
    
    # process input and output
    def input(self, c: str) -> List[str]:
        # reset the sentence, and insert it to the tree
        if c == '#':
            self.insert(self.cur_sent, 1)
            self.cur_sent = ''
            return []
        
        # update the current sentence, and do search
        self.cur_sent += c
        return self.search()
        
    

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)


'''
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

- The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
- The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences - have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
- If less than 3 hot sentences exist, then just return as many as you can.
- When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

Solution: Trie Tree
Time: 
    Search: O(max(wordlens))
    Insert: O(n)
'''
