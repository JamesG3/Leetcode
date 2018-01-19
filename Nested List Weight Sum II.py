# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSumInverse(self, nestedList):
        global maxLevel
        maxLevel = 0
        dic = {}
        
        def helper(nestedList, level):
            global maxLevel
            for l in nestedList:
                # record the lastest level
                maxLevel = min(level, maxLevel)                 
                if l.isInteger():
                    if level in dic:
                        dic[level].append(l.getInteger())
                    else:
                        dic[level] = [l.getInteger()]
                else:
                    # read nestedList from next level
                    helper(l.getList(), level-1)                

        helper(nestedList, 0)  
        weightedSUM = 0
        
        # each level in dic should be updated by adding this
        maxLevel = abs(maxLevel) + 1                            
        for level in dic:
            # calculate the weighted sum for all levels
            weightedSUM += (level + maxLevel) * sum(dic[level])     
        
        return weightedSUM
            
        
            
        
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        
        # Examples:
        # Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)
        # Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)

