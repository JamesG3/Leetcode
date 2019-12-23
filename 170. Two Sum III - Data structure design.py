class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.hashmap:
            self.hashmap[number] = 0
        self.hashmap[number] += 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for n, c in self.hashmap.items():
            diff = value - n
            if diff == n:
                if c > 1:
                    return True
            
            elif diff in self.hashmap:
                return True
            
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Solution: Hashtable
Space:  O(n)
Time:   add - O(1)
        find - O(n)

'''
