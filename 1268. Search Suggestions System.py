class Node:
    def __init__(self):
        self.next_c = {}
        self.is_word = False
        self.word = ''
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        head = Node()
        for product in products:
            node = head
            for c in product:
                if c not in node.next_c:
                    node.next_c[c] = Node()
                node = node.next_c[c]
            node.is_word = True
            node.word = product

        res = []
        node = head
        cur_str = ''
        flag = 0
        
        for c in searchWord:
            if flag:
                res.append([])
                continue
            
            if c not in node.next_c:
                res.append([])
                flag = 1
                continue
            
            node = node.next_c[c]
            bfs = [node]
            word_lst = []
            while bfs:
                tmp_bfs = []
                for bf in bfs:
                    if bf.is_word:
                        word_lst.append(bf.word)
                    tmp_bfs += [_ for _ in bf.next_c.values()]
                bfs = tmp_bfs
                
            res.append(sorted(word_lst)[:3])
            
        return res
                
'''
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
Return list of lists of the suggested products after each character of searchWord is typed. 

Solution: Trie
'''   
            
