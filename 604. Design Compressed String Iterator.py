class StringIterator:

    def __init__(self, compressedString: str):
        self.p = 0
        self.num = 0
        self.cur_c = ''
        self.compressedString = compressedString

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.num == 0:
            self.cur_c = self.compressedString[self.p]
            self.p += 1
            while self.p < len(self.compressedString) and self.compressedString[self.p].isdigit():
                self.num = 10 * self.num + int(self.compressedString[self.p])
                self.p += 1
        
        self.num -= 1
        return self.cur_c
            
    def hasNext(self) -> bool:
        return self.p != len(self.compressedString) or self.num != 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()

'''
Solution: On-demand iterator
Time: O(1)
'''
