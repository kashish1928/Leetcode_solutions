class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if(len(self.min_stack) < 1):
            self.min_stack.append(val)
        elif(val <= self.min_stack[len(self.min_stack)-1]):
            self.min_stack.append(val)
        elif(val > self.min_stack[len(self.min_stack)-1]):
            self.min_stack.append(self.min_stack[len(self.min_stack)-1])


        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if(len(self.min_stack) > 0):
            return self.min_stack[len(self.min_stack)-1]
        return 0
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()