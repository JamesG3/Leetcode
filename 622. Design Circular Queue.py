class Node:
    def __init__(self, v):
        self.val = v
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k
        self.cur_size = 0
        self.head = Node(0)
        self.tail = self.head
        
        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.size == self.cur_size:
            return False
        
        self.cur_size += 1
        node = Node(value)
        self.tail.next = node
        self.tail = node
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.cur_size == 0:
            return False
        
        self.head = self.head.next
        self.cur_size -= 1
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.cur_size == 0:
            return -1
        return self.head.next.val
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.cur_size == 0:
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.cur_size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.cur_size == self.size        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


'''
Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.

Solution: Linkedlist
'''