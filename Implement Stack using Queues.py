class MyStack(object):

    def __init__(self):
        list = []
        self.list = list
        """
        Initialize your data structure here.
        """
        

    def push(self, x):
        self.list = [x] + self.list
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        

    def pop(self):
        return self.list.pop(0)
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        

    def top(self):
        return self.list[0]
        """
        Get the top element.
        :rtype: int
        """
        

    def empty(self):
        return len(self.list) == 0
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

#push(x) -- Push element x onto stack.
#pop() -- Removes the element on top of the stack.
#top() -- Get the top element.
#empty() -- Return whether the stack is empty.
