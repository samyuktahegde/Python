class Stack:
    def __init__(self):
        self.queue = []

    def push(self, data):
        self.queue.insert(0, data)
        for i in range(0, len(self.queue)):
            self.queue.append(self.queue[0])
            self.queue.pop(0)

    def pop(self):
        if len(self.queue)>0:
            return self.queue.pop(0)
        return -1

    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
