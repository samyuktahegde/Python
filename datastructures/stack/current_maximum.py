class Stack:

    def __init__(self):
        self.stack = []
        self.trackstack = []

    def push(self, data):
        self.stack.append(data)
        if len(self.stack)==1:
            self.trackstack.append(data)
        else:
            if data>self.trackstack[-1]:
                self.trackstack.append(data)
            else:
                self.trackstack.append(self.trackstack[-1])  
        # print(self.trackstack)  

    def pop(self):
        self.trackstack.pop()
        # print(self.trackstack)  
        return self.stack.pop()

    def current_maximum(self):
        return self.trackstack[-1]

stack1 = Stack()
stack1.push(4)
stack1.push(2)
stack1.push(14)
print(stack1.current_maximum())
stack1.pop()
print(stack1.current_maximum())
stack1.push(18)
print(stack1.current_maximum())