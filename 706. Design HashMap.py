class Node:
    # 1000 max
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashtable = [Node(0, 0) for i in range(10000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        key_i = key // 100
        head = self.hashtable[key_i]
        while head.next:
            if head.next.key == key:
                head.next.val = value
                return
            
            head = head.next
        new_node = Node(key, value)
        head.next = new_node
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        key_i = key // 100
        head = self.hashtable[key_i]
        while head.next:
            if head.next.key == key:
                return head.next.val
            head = head.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        key_i = key // 100
        head = self.hashtable[key_i]
        while head.next:
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


'''
Design a HashMap without using any built-in hash table libraries.
To be specific, your design should include these functions:
put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.


Solution: Linkedlist to solve collision issue
Time: O(100)
Space: O(10000)

'''
