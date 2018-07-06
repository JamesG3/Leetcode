class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.q = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        
        self.q = [x] + self.q
        size = len(self.q)
        while size > 1:
            self.q = [self.q.pop()] + self.q
            size -= 1
            
        return
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.pop()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q == []
        

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
