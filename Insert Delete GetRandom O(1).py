# O(1) time solution with O(n) space

class RandomizedSet(object):

    def __init__(self):
        self.dic = {}
        self.l = []
        self.size = 0
        """
        Initialize your data structure here.
        """
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        if val not in self.dic:
            self.dic[val] = self.size
            self.size += 1
            self.l.append(val)
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        
        if val in self.dic:
            lastNum = self.l[self.size-1]
            if val == lastNum:
                del self.dic[val]
                self.l.pop()
            else:
                lastIndex = self.dic[lastNum]
                self.l[lastIndex], self.l[self.dic[val]] = self.l[self.dic[val]], self.l[lastIndex]
                self.dic[lastNum] = self.dic[val]
                del self.dic[val]
                self.l.pop()
            self.size -= 1
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.l[random.randrange(self.size)]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Design a data structure that supports all following operations in average O(1) time.
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
