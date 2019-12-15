# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.elements = []
        self.size = 0
        for item in nestedList:
            self._dfs(item)
        
        self.count = 0
        
    def _dfs(self, item):
        integer = item.getInteger()
        if integer != None:
            self.elements.append(integer)
            self.size += 1
            return
        
        items = item.getList()
        for i in items:
            self._dfs(i)
            
    def next(self) -> int:
        res = self.elements[self.count]
        self.count += 1
        return res
        
        
    def hasNext(self) -> bool:
        return self.count < self.size
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())



'''
Given a nested list of integers, implement an iterator to flatten it.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Solution: Traverse & Flatten
Time, Space: O(n)

'''
