class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.move()
        return self.out_stack.pop()

    def peek(self):
        self.move()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

    def move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

# Example usage:
myQueue = MyQueue()
print(myQueue.push(1))  # queue is: [1]
print(myQueue.push(2))  # queue is: [1, 2]
print(myQueue.peek())   # return 1
print(myQueue.pop())    # return 1, queue is [2]
print(myQueue.empty())  # return False
