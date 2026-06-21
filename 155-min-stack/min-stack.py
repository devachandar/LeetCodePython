class MinStack:

    def __init__(self):
        # Main stack for values, auxiliary stack for tracking minimums
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the new minimum: either val or the current min, whichever is smaller
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

        
    # def __init__(self):
    #     self.stack = []
    #     self.top_pos = -1

    # def push(self, value: int) -> None:
    #     self.stack.append(value)
    #     self.top_pos +=1

    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.top_pos -=1

    # def top(self) -> int:
    #     return self.stack[self.top_pos]

    # def getMin(self) -> int:
    #     return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()