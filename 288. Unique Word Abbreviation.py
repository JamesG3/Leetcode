class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbr_dic = {}
        for word in dictionary:
            length = len(word)
            abbr = self.to_abbr(word)
            if abbr not in self.abbr_dic:
                self.abbr_dic[abbr] = set([])
            self.abbr_dic[abbr].add(word)

    def isUnique(self, word: str) -> bool:
        wrdset = self.abbr_dic.get(self.to_abbr(word), set([]))
        if len(wrdset) == 1:
            return word in wrdset
        elif len(wrdset) == 0:
            return True
        else:
            return False
    
    
    def to_abbr(self, word):
        length = len(word)
        if length < 3:
            abbr = word
        else:
            abbr = '{}{}{}'.format(word[0], length-2, word[-1])
        return abbr
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)


'''
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

Solution: Hashtable and hashset, be careful of different scenario
Time: O(1) search, O(n) build data structure
Space: O(n)
'''
