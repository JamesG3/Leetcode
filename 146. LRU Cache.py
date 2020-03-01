class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        self.LRU = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.currsize = 0
        self.capacity = capacity
        
        
        """
        :type capacity: int
        """
        

    def get(self, key):
        if key not in self.LRU:
            return -1
        
        node = self.LRU[key]
        self.remove(node)               # update the current node by moving it to the end of linked list
        self.add(node)
        return node.val
        
        
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        
        if key not in self.LRU:
            # if len(self.LRU) == self.capacity:
            if self.currsize == self.capacity:    # if reach capacity, del from linked list and LRU dict, then insert new element
                node = self.head.next
                del self.LRU[node.key]
                self.remove(node)
                
            else:
                self.currsize += 1
            node = Node(key, value)
            
            self.add(node)
            self.LRU[key] = node
            
        else:
            node = self.LRU[key]
            self.remove(node)
            node.val = value
            self.add(node)
            self.LRU[key] = node
        
    def remove(self, node):             # remove node head.next
        node.prev.next = node.next
        node.next.prev = node.prev
        
        
    def add(self, node):                # insert node to tail.prev
        pre = self.tail.prev
        pre.next  = node
        node.prev = pre
        self.tail.prev = node
        node.next = self.tail
        
        
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
