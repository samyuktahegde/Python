class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, data):
        self.q1.insert(0,data)

    def pop(self):
        result = -1
        if len(self.q1)>0:
            while len(self.q1)>1:
                self.q2.insert(0, self.q1.pop())
            result = self.q1.pop()
            self.q1, self.q2 = self.q2, self.q1
        return result


    def print_stack(self):
        print(self.q1)

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(4)
stack.print_stack()
print(stack.pop())

    

