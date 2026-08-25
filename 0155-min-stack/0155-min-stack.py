class MinStack:
    def __init__(self):
        # Main stack to store all values
        self.stack = []
        # Auxiliary stack to store the minimum value at each state
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the smaller of the current value and the previous minimum onto the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        # Pop from both the main stack and the min_stack
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top element of the min_stack, which is the minimum
        return self.min_stack[-1]
