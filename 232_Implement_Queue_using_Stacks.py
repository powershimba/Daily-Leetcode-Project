class MyQueue(object):

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.st1.pop()


    def peek(self):
        """
        :rtype: int
        """
        return self.st1[-1]
        
    def empty(self):
        """
        :rtype: bool
        """
        if self.st1:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()