class Stack:
    def __init__(self):
        self.stack = []

# Push element into stack
def push(self, item):
    self.stack.append(item)
    print(f"{item} pushed into stack")

# Safe pop method
def safe_pop(self):
    if len(self.stack) == 0:
        print("Stack is empty, nothing to pop.")
        return None
    else:
        return self.stack.pop()

# Display stack
def display(self):
    print("Stack:", self.stack)

# Driver code
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Popped element:", s.safe_pop())
print("Popped element:", s.safe_pop())
print("Popped element:", s.safe_pop())

# Trying to pop from empty stack

print("Popped element:", s.safe_pop())