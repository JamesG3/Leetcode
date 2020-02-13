class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        self.root = {'valid': False}
        for w in dict:
            node = self.root
            for c in w:
                if c not in node:
                    node[c] = {'valid': False}
                node = node[c]
            node['valid'] = True
            
        sen_list = sentence.split(' ')
        sen_list = [self.findroot(w) for w in sen_list]
        return ' '.join(sen_list)
        
        
    def findroot(self, word):
        node = self.root
        res = ''
        for c in word:
            if node['valid']:
                return res
            if c not in node:
                return word
            else:
                res += c
            node = node[c]
        # the last one must be a word
        return res
            
            
            
'''
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.
Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.
You need to output the sentence after the replacement.

Solution: Use dict to implement prefix tree
'''
