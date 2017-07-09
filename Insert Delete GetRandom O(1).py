import random

class RandomizedSet(object):

    def __init__(self):
        self.dic = {}
        self.length = 0
        """
        Initialize your data structure here.
        """
        

    def insert(self, val):
        if val not in self.dic:
            self.dic[val] = val
            self.length += 1
            return True
        else:
            return False
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        

    def remove(self, val):
        if val in self.dic:
            self.length -= 1
            del self.dic[val]
            return True
        else:
            return False
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        

    def getRandom(self):
        return self.dic.values()[random.randrange(self.length)]
        """
        Get a random element from the set.
        :rtype: int
        """
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Design a data structure that supports all following operations in average O(1) time.
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.