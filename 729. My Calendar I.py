class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.right = None
        self.left = None

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        
        avaliable = True
        node = self.root
        while node:
            if node.start >= end:
                if not node.left:
                    node.left = Node(start, end)
                    break
                node = node.left
            elif node.end <= start:
                if not node.right:
                    node.right = Node(start, end)
                    break
                node = node.right
            else:
                return False
        
        return True
            

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


'''
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.
Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)
For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

Solution: BST
Time: O(nlogn) - O(n^2)
Space: O(n)
'''        
