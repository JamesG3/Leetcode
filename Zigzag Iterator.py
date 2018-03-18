class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.length1 = len(v1)
        self.length2 = len(v2)
        self.flag1 = 0
        self.flag2 = 0
        self.p1 = 0
        self.p2 = 0
        
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        

    def next(self):
        if self.p1 == self.length1:
            self.p2 += 1
            return self.v2[self.p2-1]
        if self.p2 == self.length2:
            self.p1 += 1
            return self.v1[self.p1-1]
        
        if self.flag1 == 0:
            self.flag1 = 1
            self.flag2 = 0
            self.p1 += 1
            return self.v1[self.p1 - 1]
            
        else:
            self.flag2 = 1
            self.flag1 = 0
            self.p2 += 1
            return self.v2[self.p2-1]
        
        """
        :rtype: int
        """

    def hasNext(self):
        return self.p1 + self.p2 < self.length1 + self.length2
                
        """
        :rtype: bool
        """
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())



# queue solution, use more space and slow, but easy to understand
class ZigzagIterator(object):
    def __init__(self, v1, v2):
        self.q = [v for v in (v1,v2) if v]
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        

    def next(self):
        v = self.q.pop(0)
        res = v.pop(0)
        if v:
            self.q.append(v)
        return res
        
        
        """
        :rtype: int
        """
        

    def hasNext(self):
        if self.q:
            return True
        return False
        """
        :rtype: bool
        """
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())



# Given two 1d vectors, implement an iterator to return their elements alternately.
# For example, given two 1d vectors:
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
