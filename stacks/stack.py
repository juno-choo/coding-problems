from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def reverse_string(self, str):
        for s in str:
            self.push(s)
        reversed_str = ''
        while not self.is_empty():
            reversed_str += self.pop()
        return reversed_str
    
    

stack = Stack()   
str = "We will rock you"
print(str)
print(stack.reverse_string(str))