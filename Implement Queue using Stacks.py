class Queue(object): 
    def __init__(self):
        self.stack1=[]        #using two stacks to reverse the sequence
        self.stack2=[]
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        self.stack1.append(x)
        """
        :type x: int
        :rtype: nothing
        """
        

    def pop(self):              #Queue: first in first out
        if len(self.stack2) != 0:
            self.stack2.pop()
        else:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            self.stack2.pop()
        """
        :rtype: nothing
        """
        

    def peek(self):
        if len(self.stack2) != 0:
            return self.stack2[-1]
        else:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
        """
        :rtype: int
        """
        

    def empty(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False
        """
        :rtype: bool
        """
        
